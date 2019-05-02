#
# PySNMP MIB module CISCOSB-File (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-File
# Produced by pysmi-0.3.4 at Wed May  1 12:22:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, TimeTicks, Bits, NotificationType, MibIdentifier, IpAddress, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "TimeTicks", "Bits", "NotificationType", "MibIdentifier", "IpAddress", "Counter64", "ModuleIdentity")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
rlFile = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96))
rlFile.setRevisions(('2013-04-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlFile.setRevisionsDescriptions(('Added MODULE-IDENTITY',))
if mibBuilder.loadTexts: rlFile.setLastUpdated('201304010000Z')
if mibBuilder.loadTexts: rlFile.setOrganization('Cisco Small Business')
if mibBuilder.loadTexts: rlFile.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Home http://www.cisco.com/smb>;, Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlFile.setDescription('The private MIB module definition for File Private Extension.')
rlFileMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlFileMibVersion.setDescription('Indicates the File System MIB version. The current version is 1.')
rlFileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 2), )
if mibBuilder.loadTexts: rlFileTable.setStatus('current')
if mibBuilder.loadTexts: rlFileTable.setDescription(' The (conceptual) table listing all the files of the flash file system.')
rlFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 2, 1), ).setIndexNames((1, "CISCOSB-File", "rlFileName"))
if mibBuilder.loadTexts: rlFileEntry.setStatus('current')
if mibBuilder.loadTexts: rlFileEntry.setDescription(' An entry (conceptual row) in the FileTable.')
rlFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileName.setStatus('current')
if mibBuilder.loadTexts: rlFileName.setDescription('The name of the file.')
rlFilePermission = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("read", 1), ("write", 2), ("readWrite", 3), ("noReadNoWrite", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFilePermission.setStatus('current')
if mibBuilder.loadTexts: rlFilePermission.setDescription('Specifies the permission level in which this file can be accessed. ')
rlFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileSize.setStatus('current')
if mibBuilder.loadTexts: rlFileSize.setDescription('The size of the file in bytes (actual size).')
rlFileModificationDate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileModificationDate.setStatus('current')
if mibBuilder.loadTexts: rlFileModificationDate.setDescription('The time-stamp indicating the date of creation or last modification of this file. The format of the time-stamp is dd-mmm-yyyy')
rlFileModificationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileModificationTime.setStatus('current')
if mibBuilder.loadTexts: rlFileModificationTime.setDescription('The time-stamp indicating the time of creation or last modification of this file. The format of the time-stamp is hh:mm:ss')
rlFileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlFileRowStatus.setDescription('It is used just to delete an entry')
rlFileFlashSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileFlashSize.setStatus('current')
if mibBuilder.loadTexts: rlFileFlashSize.setDescription('The size allocated for the file in bytes (allocated size).')
rlFileFullNormalizedName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 2, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileFullNormalizedName.setStatus('current')
if mibBuilder.loadTexts: rlFileFullNormalizedName.setDescription("The full normalized name - up to max OCTET STRING length and not containing '..' and '.' path components.")
rlFileActionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 3), )
if mibBuilder.loadTexts: rlFileActionTable.setStatus('current')
if mibBuilder.loadTexts: rlFileActionTable.setDescription(' The (conceptual) table listing only one entry at a time with parameters needed for performing an action on a file.')
rlFileActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 3, 1), ).setIndexNames((0, "CISCOSB-File", "rlFileActionName"))
if mibBuilder.loadTexts: rlFileActionEntry.setStatus('current')
if mibBuilder.loadTexts: rlFileActionEntry.setDescription(' An entry (conceptual row) in the FileActionTable.')
rlFileActionName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileActionName.setStatus('current')
if mibBuilder.loadTexts: rlFileActionName.setDescription('The name of the file.')
rlFileActionNewName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileActionNewName.setStatus('current')
if mibBuilder.loadTexts: rlFileActionNewName.setDescription('The new name for the file (in case of action rename).')
rlFileActionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 3, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileActionRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlFileActionRowStatus.setDescription('It is used to create an entry')
rlFileActionCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("rename", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileActionCommand.setStatus('current')
if mibBuilder.loadTexts: rlFileActionCommand.setDescription('Perform an action on the file.')
rlFileTotalSizeOfFlash = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileTotalSizeOfFlash.setStatus('current')
if mibBuilder.loadTexts: rlFileTotalSizeOfFlash.setDescription('Indicates the total size of the flash in bytes.')
rlFileFreeSizeOfFlash = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileFreeSizeOfFlash.setStatus('current')
if mibBuilder.loadTexts: rlFileFreeSizeOfFlash.setDescription('Indicates the number of free bytes in the flash.')
rlFileAuditingEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileAuditingEnable.setStatus('current')
if mibBuilder.loadTexts: rlFileAuditingEnable.setDescription('Controls whether SysLog messages should be issued on file rename/delete events')
mibBuilder.exportSymbols("CISCOSB-File", rlFileRowStatus=rlFileRowStatus, rlFileModificationTime=rlFileModificationTime, rlFileActionEntry=rlFileActionEntry, rlFile=rlFile, rlFileActionCommand=rlFileActionCommand, rlFileActionRowStatus=rlFileActionRowStatus, rlFileAuditingEnable=rlFileAuditingEnable, rlFileTable=rlFileTable, rlFileSize=rlFileSize, rlFileModificationDate=rlFileModificationDate, rlFileEntry=rlFileEntry, rlFileFreeSizeOfFlash=rlFileFreeSizeOfFlash, rlFileActionNewName=rlFileActionNewName, rlFileTotalSizeOfFlash=rlFileTotalSizeOfFlash, PYSNMP_MODULE_ID=rlFile, rlFileMibVersion=rlFileMibVersion, rlFileFlashSize=rlFileFlashSize, rlFileFullNormalizedName=rlFileFullNormalizedName, rlFileName=rlFileName, rlFilePermission=rlFilePermission, rlFileActionTable=rlFileActionTable, rlFileActionName=rlFileActionName)
