#
# PySNMP MIB module SONOMASYSTEMS-SONOMA-IPAPPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONOMASYSTEMS-SONOMA-IPAPPS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:09:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, Counter32, Integer32, IpAddress, iso, Counter64, ObjectIdentity, TimeTicks, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "Counter32", "Integer32", "IpAddress", "iso", "Counter64", "ObjectIdentity", "TimeTicks", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonomaApplications, = mibBuilder.importSymbols("SONOMASYSTEMS-SONOMA-MIB", "sonomaApplications")
ipApplications = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1))
bootpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1))
pingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2))
class DisplayString(OctetString):
    pass

tftpFileServerIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpFileServerIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: tftpFileServerIpAddress.setDescription('The IP Address of the file server to use for image and parameter file downloads and uploads.')
tftpFileName = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpFileName.setStatus('mandatory')
if mibBuilder.loadTexts: tftpFileName.setDescription('The path and name of the file to be uploaded or downloaded. This string is 128 charachters long, any longer causes problems fro Windown NT or Windows 95. This length is recommended in RFC 1542.')
tftpImageNumber = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("image1", 1), ("image2", 2), ("image3", 3), ("image4", 4), ("image5", 5), ("image6", 6), ("image7", 7), ("image8", 8))).clone('image1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpImageNumber.setStatus('mandatory')
if mibBuilder.loadTexts: tftpImageNumber.setDescription('The Image number (1 - 8) for the operational image file to be downloaded to. In the case of BOOTP the image will be stored in the BOOTP/ directory in flash')
tftpFileAction = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("noAction", 1), ("startBootPImageDownload", 2), ("startTFTPImageDownload", 3), ("startPrimaryImageTFTPDownload", 4), ("startSecondaryImageTFTPDownload", 5), ("startTFTPParameterBinDownload", 6), ("startTFTPParameterTextDownload", 7), ("startTFTPParameterBinUpload", 8), ("startTFTPParameterTextUpload", 9), ("startTFTPProfileDownload", 10))).clone('noAction')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpFileAction.setStatus('mandatory')
if mibBuilder.loadTexts: tftpFileAction.setDescription("This object is used to initiate file transfer between this unit and the file server identified by tftpFileServerIpAddress. A download indicates that the file transfer is from the file server (down) to the device. An upload indicates a file transfer from the device (up) to the server. This object can be used to initiate either image or parameter file downloads and a parameter file upload. There is no image file upload feature. An image file can be downloaded via either a BootP request (where the image filename and the BootP server's IP Address is unknown) or via a TFTP request where the user has configured the tftpFileName object with the path and name of the file. BootP cannot be used to download or upload a parameter file. An attempt to set this object to one of the following values: startTFTPImageDownload, startTFTPParameterDownload or startTFTPParameterUpload, will fail if either the tftpFileName or tftpFileServerIpAddress object has not bee configured. The tftpFileName and tftpFileServerIpAddress objects are ignored for BootP requests. A value of noAction is always returned to a GetRequest. Seting this object with a value of noAction has no effect. The startPrimaryImageTFTPDownload is used to initiate the download of the primary boot image. This image is only downloaded when there is a new revision of the basic boot mechanism or changes to the flash or CMOS sub-systems.")
tftpFileTransferStatus = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))).clone(namedValues=NamedValues(("idle", 1), ("downloading", 2), ("uploading", 3), ("programmingflash", 4), ("failBootpNoServer", 5), ("failTFTPNoFile", 6), ("errorServerResponse", 7), ("failTFTPInvalidFile", 8), ("failNetworkTimeout", 9), ("failFlashProgError", 10), ("failFlashChksumError", 11), ("errorServerData", 12), ("uploadResultUnknown", 13), ("uploadSuccessful", 14), ("downloadSuccessful", 15), ("generalFailure", 16), ("failCannotOverwriteActiveImage", 17), ("failCannotOverwriteActiveParam", 18)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tftpFileTransferStatus.setStatus('mandatory')
if mibBuilder.loadTexts: tftpFileTransferStatus.setDescription('This is the current status of the file transfer process.')
pingIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: pingIpAddress.setDescription(' The IP Address to Ping')
pingTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: pingTimeout.setDescription('This is the timeout, in seconds, for a ping.')
pingRetries = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2, 3), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingRetries.setStatus('mandatory')
if mibBuilder.loadTexts: pingRetries.setDescription(' This value indicates the number of times, to ping. A value of 1 is the default and insicates that the unit will send one pingp. 0 means no action.')
pingStatus = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pingStatus.setStatus('mandatory')
if mibBuilder.loadTexts: pingStatus.setDescription(' A text string which indicates the result or status of the last ping which the unit sent.')
pingAction = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("start", 1), ("stop", 2), ("noAction", 3))).clone('noAction')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingAction.setStatus('mandatory')
if mibBuilder.loadTexts: pingAction.setDescription('Indicates whether to stop or start a ping. This always returns the value noAction to a Get Request.')
mibBuilder.exportSymbols("SONOMASYSTEMS-SONOMA-IPAPPS-MIB", tftpFileTransferStatus=tftpFileTransferStatus, tftpImageNumber=tftpImageNumber, pingRetries=pingRetries, pingGroup=pingGroup, ipApplications=ipApplications, tftpFileAction=tftpFileAction, tftpFileServerIpAddress=tftpFileServerIpAddress, pingTimeout=pingTimeout, pingAction=pingAction, pingStatus=pingStatus, pingIpAddress=pingIpAddress, bootpGroup=bootpGroup, DisplayString=DisplayString, tftpFileName=tftpFileName)
