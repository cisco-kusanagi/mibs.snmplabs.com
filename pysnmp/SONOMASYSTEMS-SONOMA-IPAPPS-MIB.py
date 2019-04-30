#
# PySNMP MIB module SONOMASYSTEMS-SONOMA-IPAPPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONOMASYSTEMS-SONOMA-IPAPPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:01:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, Bits, MibIdentifier, iso, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, ObjectIdentity, Counter32, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "Bits", "MibIdentifier", "iso", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "ObjectIdentity", "Counter32", "IpAddress", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonomaApplications, = mibBuilder.importSymbols("SONOMASYSTEMS-SONOMA-MIB", "sonomaApplications")
ipApplications = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1))
bootpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1))
pingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2))
class DisplayString(OctetString):
    pass

tftpFileServerIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpFileServerIpAddress.setStatus('mandatory')
tftpFileName = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpFileName.setStatus('mandatory')
tftpImageNumber = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("image1", 1), ("image2", 2), ("image3", 3), ("image4", 4), ("image5", 5), ("image6", 6), ("image7", 7), ("image8", 8))).clone('image1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpImageNumber.setStatus('mandatory')
tftpFileAction = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("noAction", 1), ("startBootPImageDownload", 2), ("startTFTPImageDownload", 3), ("startPrimaryImageTFTPDownload", 4), ("startSecondaryImageTFTPDownload", 5), ("startTFTPParameterBinDownload", 6), ("startTFTPParameterTextDownload", 7), ("startTFTPParameterBinUpload", 8), ("startTFTPParameterTextUpload", 9), ("startTFTPProfileDownload", 10))).clone('noAction')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpFileAction.setStatus('mandatory')
tftpFileTransferStatus = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))).clone(namedValues=NamedValues(("idle", 1), ("downloading", 2), ("uploading", 3), ("programmingflash", 4), ("failBootpNoServer", 5), ("failTFTPNoFile", 6), ("errorServerResponse", 7), ("failTFTPInvalidFile", 8), ("failNetworkTimeout", 9), ("failFlashProgError", 10), ("failFlashChksumError", 11), ("errorServerData", 12), ("uploadResultUnknown", 13), ("uploadSuccessful", 14), ("downloadSuccessful", 15), ("generalFailure", 16), ("failCannotOverwriteActiveImage", 17), ("failCannotOverwriteActiveParam", 18)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tftpFileTransferStatus.setStatus('mandatory')
pingIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingIpAddress.setStatus('mandatory')
pingTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingTimeout.setStatus('mandatory')
pingRetries = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2, 3), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingRetries.setStatus('mandatory')
pingStatus = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pingStatus.setStatus('mandatory')
pingAction = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 8, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("start", 1), ("stop", 2), ("noAction", 3))).clone('noAction')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pingAction.setStatus('mandatory')
mibBuilder.exportSymbols("SONOMASYSTEMS-SONOMA-IPAPPS-MIB", bootpGroup=bootpGroup, ipApplications=ipApplications, pingGroup=pingGroup, pingStatus=pingStatus, tftpFileServerIpAddress=tftpFileServerIpAddress, tftpFileAction=tftpFileAction, pingTimeout=pingTimeout, tftpFileTransferStatus=tftpFileTransferStatus, tftpFileName=tftpFileName, pingIpAddress=pingIpAddress, tftpImageNumber=tftpImageNumber, pingRetries=pingRetries, pingAction=pingAction, DisplayString=DisplayString)
