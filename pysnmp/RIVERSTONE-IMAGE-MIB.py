#
# PySNMP MIB module RIVERSTONE-IMAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-IMAGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:49:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
riverstoneMibs, = mibBuilder.importSymbols("RIVERSTONE-SMI-MIB", "riverstoneMibs")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, MibIdentifier, NotificationType, Unsigned32, ModuleIdentity, Gauge32, Integer32, Counter64, TimeTicks, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "MibIdentifier", "NotificationType", "Unsigned32", "ModuleIdentity", "Gauge32", "Integer32", "Counter64", "TimeTicks", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
rsImageMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 2, 13))
rsImageMib.setRevisions(('2001-03-16 00:00',))
if mibBuilder.loadTexts: rsImageMib.setLastUpdated('200103160000Z')
if mibBuilder.loadTexts: rsImageMib.setOrganization('Riverstone Networks, Inc')
class RsImageMibErrorCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("noInfo", 1), ("successfullyCompleted", 2), ("timeout", 3), ("networkError", 4), ("noSpace", 5), ("invalidImage", 6), ("commandCompleted", 7), ("internalError", 8), ("tftpServerError", 9))

class RsImageMibControlModuleIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("primaryCM", 1), ("backupCM", 2))

class RsImageMibSlotIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("slot0", 1), ("slot1", 2))

class RsImageMibImageIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("firstImage", 1), ("secondImage", 2), ("thirdImage", 3))

class RsImageMibChosen(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noInfo", 1), ("chosen", 2), ("notChosen", 3))

rsImageMibAction = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 13, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noop", 1), ("addImageToAgent", 2), ("deleteImageFromAgent", 3), ("chooseImageOnAgent", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsImageMibAction.setStatus('current')
rsImageMibTftpServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 13, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsImageMibTftpServerAddress.setStatus('current')
rsImageMibHostName = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 13, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsImageMibHostName.setStatus('current')
rsImageMibTftpUrl = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 13, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsImageMibTftpUrl.setStatus('current')
rsImageMibImageName = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 13, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsImageMibImageName.setStatus('current')
rsImageMibDestination = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 13, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("both", 1), ("pCM", 2), ("bCM", 3), ("pCMslot0", 4), ("pCMslot1", 5), ("bCMslot0", 6), ("bCMslot1", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsImageMibDestination.setStatus('current')
rsImageMibActivateTransfer = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 13, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsImageMibActivateTransfer.setStatus('current')
rsImageMibPrimaryCMOperationStatus = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 13, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("idle", 1), ("adding", 2), ("deleting", 3), ("choosing", 4), ("actionComplete", 5), ("error", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsImageMibPrimaryCMOperationStatus.setStatus('current')
rsImageMibBackupCMOperationStatus = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 13, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("idle", 1), ("adding", 2), ("deleting", 3), ("choosing", 4), ("actionComplete", 5), ("error", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsImageMibBackupCMOperationStatus.setStatus('current')
rsImageMibPrimaryCMLastError = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 13, 10), RsImageMibErrorCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsImageMibPrimaryCMLastError.setStatus('current')
rsImageMibBackupCMLastError = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 13, 11), RsImageMibErrorCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsImageMibBackupCMLastError.setStatus('current')
rsImageMibPrimaryCMLastErrorString = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 13, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsImageMibPrimaryCMLastErrorString.setStatus('current')
rsImageMibBackupCMLastErrorString = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 13, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsImageMibBackupCMLastErrorString.setStatus('current')
rsImageMibListTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 13, 14), )
if mibBuilder.loadTexts: rsImageMibListTable.setStatus('current')
rsImageMibListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 13, 14, 1), ).setIndexNames((0, "RIVERSTONE-IMAGE-MIB", "rsImageMibControlModuleIndex"), (0, "RIVERSTONE-IMAGE-MIB", "rsImageMibSlotIndex"), (0, "RIVERSTONE-IMAGE-MIB", "rsImageMibImageIndex"))
if mibBuilder.loadTexts: rsImageMibListEntry.setStatus('current')
rsImageMibControlModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 13, 14, 1, 1), RsImageMibControlModuleIndex())
if mibBuilder.loadTexts: rsImageMibControlModuleIndex.setStatus('current')
rsImageMibSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 13, 14, 1, 2), RsImageMibSlotIndex())
if mibBuilder.loadTexts: rsImageMibSlotIndex.setStatus('current')
rsImageMibImageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 13, 14, 1, 3), RsImageMibImageIndex())
if mibBuilder.loadTexts: rsImageMibImageIndex.setStatus('current')
rsImageMibListImageName = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 13, 14, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsImageMibListImageName.setStatus('current')
rsImageMibVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 13, 14, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsImageMibVersion.setStatus('current')
rsImageMibChosen = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 13, 14, 1, 6), RsImageMibChosen()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsImageMibChosen.setStatus('current')
rsImageMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 13, 15))
rsImageMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 13, 15, 1))
rsImageMibCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 13, 15, 2))
rsImageMibAddDeleteChooseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 13, 15, 1, 1)).setObjects(("RIVERSTONE-IMAGE-MIB", "rsImageMibAction"), ("RIVERSTONE-IMAGE-MIB", "rsImageMibTftpServerAddress"), ("RIVERSTONE-IMAGE-MIB", "rsImageMibHostName"), ("RIVERSTONE-IMAGE-MIB", "rsImageMibTftpUrl"), ("RIVERSTONE-IMAGE-MIB", "rsImageMibImageName"), ("RIVERSTONE-IMAGE-MIB", "rsImageMibDestination"), ("RIVERSTONE-IMAGE-MIB", "rsImageMibActivateTransfer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsImageMibAddDeleteChooseGroup = rsImageMibAddDeleteChooseGroup.setStatus('current')
rsImageMibListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 13, 15, 1, 2)).setObjects(("RIVERSTONE-IMAGE-MIB", "rsImageMibListImageName"), ("RIVERSTONE-IMAGE-MIB", "rsImageMibVersion"), ("RIVERSTONE-IMAGE-MIB", "rsImageMibChosen"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsImageMibListGroup = rsImageMibListGroup.setStatus('current')
rsImageMibStatusAndErrorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 13, 15, 1, 3)).setObjects(("RIVERSTONE-IMAGE-MIB", "rsImageMibPrimaryCMOperationStatus"), ("RIVERSTONE-IMAGE-MIB", "rsImageMibBackupCMOperationStatus"), ("RIVERSTONE-IMAGE-MIB", "rsImageMibPrimaryCMLastError"), ("RIVERSTONE-IMAGE-MIB", "rsImageMibBackupCMLastError"), ("RIVERSTONE-IMAGE-MIB", "rsImageMibPrimaryCMLastErrorString"), ("RIVERSTONE-IMAGE-MIB", "rsImageMibBackupCMLastErrorString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsImageMibStatusAndErrorGroup = rsImageMibStatusAndErrorGroup.setStatus('current')
rsImageMibBasicComplianceV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5567, 2, 13, 15, 2, 1)).setObjects(("RIVERSTONE-IMAGE-MIB", "rsImageMibAddDeleteChooseGroup"), ("RIVERSTONE-IMAGE-MIB", "rsImageMibListGroup"), ("RIVERSTONE-IMAGE-MIB", "rsImageMibStatusAndErrorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsImageMibBasicComplianceV1 = rsImageMibBasicComplianceV1.setStatus('current')
mibBuilder.exportSymbols("RIVERSTONE-IMAGE-MIB", rsImageMib=rsImageMib, rsImageMibTftpServerAddress=rsImageMibTftpServerAddress, rsImageMibPrimaryCMOperationStatus=rsImageMibPrimaryCMOperationStatus, rsImageMibChosen=rsImageMibChosen, rsImageMibAddDeleteChooseGroup=rsImageMibAddDeleteChooseGroup, rsImageMibListGroup=rsImageMibListGroup, rsImageMibStatusAndErrorGroup=rsImageMibStatusAndErrorGroup, rsImageMibVersion=rsImageMibVersion, rsImageMibBackupCMOperationStatus=rsImageMibBackupCMOperationStatus, rsImageMibPrimaryCMLastErrorString=rsImageMibPrimaryCMLastErrorString, rsImageMibBackupCMLastError=rsImageMibBackupCMLastError, rsImageMibControlModuleIndex=rsImageMibControlModuleIndex, RsImageMibSlotIndex=RsImageMibSlotIndex, rsImageMibDestination=rsImageMibDestination, rsImageMibBackupCMLastErrorString=rsImageMibBackupCMLastErrorString, rsImageMibGroups=rsImageMibGroups, rsImageMibImageName=rsImageMibImageName, rsImageMibListImageName=rsImageMibListImageName, rsImageMibSlotIndex=rsImageMibSlotIndex, RsImageMibImageIndex=RsImageMibImageIndex, PYSNMP_MODULE_ID=rsImageMib, RsImageMibControlModuleIndex=RsImageMibControlModuleIndex, RsImageMibErrorCode=RsImageMibErrorCode, rsImageMibCompliance=rsImageMibCompliance, rsImageMibActivateTransfer=rsImageMibActivateTransfer, rsImageMibListEntry=rsImageMibListEntry, rsImageMibConformance=rsImageMibConformance, rsImageMibBasicComplianceV1=rsImageMibBasicComplianceV1, rsImageMibHostName=rsImageMibHostName, rsImageMibListTable=rsImageMibListTable, RsImageMibChosen=RsImageMibChosen, rsImageMibTftpUrl=rsImageMibTftpUrl, rsImageMibPrimaryCMLastError=rsImageMibPrimaryCMLastError, rsImageMibAction=rsImageMibAction, rsImageMibImageIndex=rsImageMibImageIndex)
