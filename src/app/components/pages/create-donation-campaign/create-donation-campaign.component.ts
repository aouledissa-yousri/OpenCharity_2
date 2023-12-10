import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { FileHelper } from 'src/app/helpers/FileHelper';
import { IpfsHelper } from 'src/app/helpers/IpfsHelper';
import { DonationCampaignManagementService } from 'src/app/services/DonationCampaignManagementService/donation-campaign-management.service';
import { UserManagementService } from 'src/app/services/UserManagementService/user-management.service';
import { WalletService } from 'src/app/services/WalletService/wallet.service';
import { LoadingDialogComponent } from '../../dialogs/loading-dialog/loading-dialog.component';
import { ResultDialogComponent } from '../../dialogs/result-dialog/result-dialog.component';

@Component({
  selector: 'app-create-donation-campaign',
  templateUrl: './create-donation-campaign.component.html',
  styleUrls: ['./create-donation-campaign.component.scss']
})
export class CreateDonationCampaignComponent {

  donationCampaignForm!: FormGroup;
  defaultImage = "../../../../assets/placeholder.png"
  image!: File

  constructor(
    private donationCampaignManagementService: DonationCampaignManagementService,
    private walletService: WalletService,
    private formBuilder: FormBuilder,
    private dialog: MatDialog
  ){}

  ngOnInit(): void {
      this.initForm()
  }

  public initForm(){
    this.donationCampaignForm = this.formBuilder.group({
      title: ["", Validators.required],
      image: [null, Validators.required],
      wallpaper: [""],
      description: ["", Validators.required]
    })
  }

  public async displayImage(event: any){
    const file = event.target.files[0]
    this.defaultImage = await FileHelper.getFilePath(file)
    this.image = file
  }

  public isValid() {
    return this.donationCampaignForm.value.title !== "" && 
           this.donationCampaignForm.value.image !== null &&
           this.donationCampaignForm.value.description !== ""
  }


  public reset(){
    this.defaultImage = "../../../../assets/placeholder.png"
    this.donationCampaignForm.reset({
      title: "",
      description: "",
      wallpaper: "",
      image: null
    })
  }


  public async addDonationCampaign(){

    let dialogRef: any = this.dialog.open(LoadingDialogComponent, {data: "Creating Donation Campaign..."})

    this.donationCampaignForm.patchValue({
      wallpaper: await IpfsHelper.uploadFile(this.image)
    })

    if(this.walletService.getWalletAddress() === null) this.walletService.connectWallet((window as any).ethereum)
    await this.donationCampaignManagementService.addDonationCampaign(
      this.donationCampaignForm.value.title,
      this.donationCampaignForm.value.wallpaper,
      this.donationCampaignForm.value.description
    )

    dialogRef.close()
    this.donationCampaignForm.reset()

    dialogRef = this.dialog.open(ResultDialogComponent, {data: {
      title: "Donation Campaign Has Been Created!!",
      description: "Your donation campaign has been created successfully"
    }})


  }

}