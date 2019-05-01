#
# PySNMP MIB module WWP-FILE-TRANSFER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-FILE-TRANSFER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:37:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, iso, ModuleIdentity, NotificationType, Bits, Gauge32, MibIdentifier, ObjectIdentity, Unsigned32, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "iso", "ModuleIdentity", "NotificationType", "Bits", "Gauge32", "MibIdentifier", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress")
DateAndTime, MacAddress, TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "MacAddress", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpFileTransferMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 7))
wwpFileTransferMIB.setRevisions(('2001-04-03 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wwpFileTransferMIB.setRevisionsDescriptions(('Initial creation.',))
if mibBuilder.loadTexts: wwpFileTransferMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpFileTransferMIB.setOrganization('World Wide Packets, Inc')
if mibBuilder.loadTexts: wwpFileTransferMIB.setContactInfo(' Mib Meister Postal: World Wide Packets P.O. Box 950 Veradale, WA 99037 USA Phone: +1 509 242 9000 Email: mib.meister@worldwidepackets.com')
if mibBuilder.loadTexts: wwpFileTransferMIB.setDescription('The MIB module for the WWP TFTP Operation to download a file.')
wwpFileTransferMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1))
wwpFileTransfer = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1))
wwpFileTransferMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 7, 2))
wwpFiletransferMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 7, 2, 0))
wwpFileTransferMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 7, 3))
wwpFileTransferMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 7, 3, 1))
wwpFileTransferMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 7, 3, 2))
class FileTransferState(TextualConvention, Integer32):
    description = 'The state of a File transfer operation. The description of each state is given below: idle: No file transfer operation is in place. sending: this state signifies that the file is being sent to the tftp server. receiving: this state signifies that the file is being received from the tftp server. transferComplete: the state when a file transfer request is successfully completed. failed: the file transfer request was unsuccesful. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("idle", 1), ("sending", 2), ("receiving", 3), ("transferComplete", 4), ("failed", 5))

class FileTransferFailCause(TextualConvention, Integer32):
    description = 'The reason a File transfer request failed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("noStatus", 1), ("timeout", 2), ("networkError", 3), ("noSpace", 4), ("invalidFileName", 5), ("commandCompleted", 6), ("internalError", 7), ("commandFileParseError", 8))

wwpFTransferOp = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("sendFile", 1), ("getFile", 2), ("getCmdFile", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpFTransferOp.setStatus('current')
if mibBuilder.loadTexts: wwpFTransferOp.setDescription('Used to transfer file(s) between a TFTP server (remote) and the device(local). All transfers are binary. There are three types of file transfers: sendFile sends a file to the host TFTP server. getFile receives a file from the host server. getCmdFile gets the specified file from the host and parses that file for additional operations to be performed. This is the mechanism used to upgrade the device with new software.')
wwpFTransferServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpFTransferServerAddr.setStatus('current')
if mibBuilder.loadTexts: wwpFTransferServerAddr.setDescription('The ip address of the tftp server from (or to) which to transfer the file.Address must be a unicast address that is reachable from the agent and no firewalls/acls preventing tftp datagrams from being transferred.')
wwpFTransferRemoteFilename = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpFTransferRemoteFilename.setStatus('current')
if mibBuilder.loadTexts: wwpFTransferRemoteFilename.setDescription('The file name (including the path, if applicable) to be retrieved from the tftp server. If the switch/device is downloading a file , then this should be name of the file on the remote server. Length of filename string must not exceed 255 alpha-numeric characters, no spaces in filenames.')
wwpFTransferLocalFilename = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpFTransferLocalFilename.setStatus('current')
if mibBuilder.loadTexts: wwpFTransferLocalFilename.setDescription('The file name (including the path, if applicable) to be written to. If the switch/device is downloading a file ,then this should be name of the file on the switch/device. Length of filename string must not exceed 255 alpha-numeric characters, no spaces in filenames. By default it will have the same value as of wwpFTransferRemoteFilename.')
wwpFTransferActivate = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpFTransferActivate.setStatus('current')
if mibBuilder.loadTexts: wwpFTransferActivate.setDescription("Activate the file transfer operation with a value of True(1). The object will return to 'false' once the file transfer is completed. Poll wwpFTransferStatus for current status. Default value is False. wwpFTransferRemoteFileName, wwpFTransferServerAddress and wwpFTransferOp must be valid prior to setting this object to True.")
wwpFTransferNotifOnCompletion = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpFTransferNotifOnCompletion.setStatus('current')
if mibBuilder.loadTexts: wwpFTransferNotifOnCompletion.setDescription('Specifies whether or not a wwpFTransferCompletion notification should be issued on completion of the tftp transfer. If such a notification is desired, it is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered.')
wwpFTransferStatus = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 7), FileTransferState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpFTransferStatus.setStatus('current')
if mibBuilder.loadTexts: wwpFTransferStatus.setDescription("Specifies the state of this file transfer request. If no file transfer request is being processed , then the wwpFTransferStatus should be 'idle'.")
wwpFTransferFailCause = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 8), FileTransferFailCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpFTransferFailCause.setStatus('current')
if mibBuilder.loadTexts: wwpFTransferFailCause.setDescription("The reason why the file transfer operation failed. If no file transfer request is being processed , then the wwpFTransferFileCause should be 'noStatus'.")
wwpFTransferNotificationStatus = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("downloadSuccess", 0), ("tftpServerNotFound", 1), ("couldNotGetFile", 2), ("cmdFileParseError", 3), ("internalFilesystemError", 4), ("inValidFileContents", 5), ("flashOffline", 6), ("noStatus", 7), ("putSuccessful", 8), ("couldNotPutFile", 9), ("badFileCrc", 10), ("allFilesSkipped", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpFTransferNotificationStatus.setStatus('current')
if mibBuilder.loadTexts: wwpFTransferNotificationStatus.setDescription('The status of the file transfer which is to be reported via the FileTransfer Notification.')
wwpFTransferNotificationInfo = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 7, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpFTransferNotificationInfo.setStatus('current')
if mibBuilder.loadTexts: wwpFTransferNotificationInfo.setDescription('The string explaining the error code in detail or the additional info for the file transfer completion.')
wwpFTransferCompletion = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 7, 2, 0, 1)).setObjects(("WWP-FILE-TRANSFER-MIB", "wwpFTransferRemoteFilename"), ("WWP-FILE-TRANSFER-MIB", "wwpFTransferLocalFilename"), ("WWP-FILE-TRANSFER-MIB", "wwpFTransferNotificationStatus"), ("WWP-FILE-TRANSFER-MIB", "wwpFTransferNotificationInfo"))
if mibBuilder.loadTexts: wwpFTransferCompletion.setStatus('current')
if mibBuilder.loadTexts: wwpFTransferCompletion.setDescription('A wwpFTransferCompletion notification is sent at the completion of a file transfer request.')
wwpFTransferCmdParseError = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 7, 2, 0, 2)).setObjects(("WWP-FILE-TRANSFER-MIB", "wwpFTransferRemoteFilename"))
if mibBuilder.loadTexts: wwpFTransferCmdParseError.setStatus('deprecated')
if mibBuilder.loadTexts: wwpFTransferCmdParseError.setDescription('A wwpFTransferCmdParseError notification is sent if the parsing of the cmd file returns an error.')
mibBuilder.exportSymbols("WWP-FILE-TRANSFER-MIB", wwpFTransferLocalFilename=wwpFTransferLocalFilename, FileTransferState=FileTransferState, wwpFileTransferMIB=wwpFileTransferMIB, wwpFileTransferMIBGroups=wwpFileTransferMIBGroups, wwpFileTransferMIBCompliances=wwpFileTransferMIBCompliances, wwpFTransferNotificationInfo=wwpFTransferNotificationInfo, wwpFTransferCmdParseError=wwpFTransferCmdParseError, wwpFTransferOp=wwpFTransferOp, wwpFTransferStatus=wwpFTransferStatus, wwpFiletransferMIBNotifications=wwpFiletransferMIBNotifications, FileTransferFailCause=FileTransferFailCause, wwpFileTransferMIBConformance=wwpFileTransferMIBConformance, wwpFTransferActivate=wwpFTransferActivate, wwpFTransferCompletion=wwpFTransferCompletion, wwpFTransferNotificationStatus=wwpFTransferNotificationStatus, wwpFileTransferMIBObjects=wwpFileTransferMIBObjects, wwpFTransferNotifOnCompletion=wwpFTransferNotifOnCompletion, PYSNMP_MODULE_ID=wwpFileTransferMIB, wwpFileTransferMIBNotificationPrefix=wwpFileTransferMIBNotificationPrefix, wwpFTransferFailCause=wwpFTransferFailCause, wwpFTransferRemoteFilename=wwpFTransferRemoteFilename, wwpFTransferServerAddr=wwpFTransferServerAddr, wwpFileTransfer=wwpFileTransfer)
