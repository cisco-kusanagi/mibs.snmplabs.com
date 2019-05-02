#
# PySNMP MIB module ASCEND-MIBTACL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBTACL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:28:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Bits, Counter64, NotificationType, iso, Gauge32, ObjectIdentity, IpAddress, ModuleIdentity, Counter32, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Bits", "Counter64", "NotificationType", "iso", "Gauge32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Counter32", "MibIdentifier", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibtaclProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 128))
mibtaclProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 128, 1), )
if mibBuilder.loadTexts: mibtaclProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibtaclProfileTable.setDescription('A list of mibtaclProfile profile entries.')
mibtaclProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 128, 1, 1), ).setIndexNames((0, "ASCEND-MIBTACL-MIB", "taclProfile-Index-o"))
if mibBuilder.loadTexts: mibtaclProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibtaclProfileEntry.setDescription('A mibtaclProfile entry containing objects that maps to the parameters of mibtaclProfile profile.')
taclProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 128, 1, 1, 1), Integer32()).setLabel("taclProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: taclProfile_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: taclProfile_Index_o.setDescription('')
taclProfile_EnablePermit = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 128, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("taclProfile-EnablePermit").setMaxAccess("readwrite")
if mibBuilder.loadTexts: taclProfile_EnablePermit.setStatus('mandatory')
if mibBuilder.loadTexts: taclProfile_EnablePermit.setDescription('When TRUE, the permit-list is used, when FALSE, the permit-list is skipped when filtering.')
taclProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 128, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("taclProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: taclProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: taclProfile_Action_o.setDescription('')
mibtaclProfile_PermitListTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 128, 2), ).setLabel("mibtaclProfile-PermitListTable")
if mibBuilder.loadTexts: mibtaclProfile_PermitListTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibtaclProfile_PermitListTable.setDescription('A list of mibtaclProfile__permit_list profile entries.')
mibtaclProfile_PermitListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1), ).setLabel("mibtaclProfile-PermitListEntry").setIndexNames((0, "ASCEND-MIBTACL-MIB", "taclProfile-PermitList-Index-o"), (0, "ASCEND-MIBTACL-MIB", "taclProfile-PermitList-Index1-o"))
if mibBuilder.loadTexts: mibtaclProfile_PermitListEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibtaclProfile_PermitListEntry.setDescription('A mibtaclProfile__permit_list entry containing objects that maps to the parameters of mibtaclProfile__permit_list profile.')
taclProfile_PermitList_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1, 1), Integer32()).setLabel("taclProfile-PermitList-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: taclProfile_PermitList_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: taclProfile_PermitList_Index_o.setDescription('')
taclProfile_PermitList_Index1_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1, 2), Integer32()).setLabel("taclProfile-PermitList-Index1-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: taclProfile_PermitList_Index1_o.setStatus('mandatory')
if mibBuilder.loadTexts: taclProfile_PermitList_Index1_o.setDescription('')
taclProfile_PermitList_ValidEntry = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("taclProfile-PermitList-ValidEntry").setMaxAccess("readwrite")
if mibBuilder.loadTexts: taclProfile_PermitList_ValidEntry.setStatus('mandatory')
if mibBuilder.loadTexts: taclProfile_PermitList_ValidEntry.setDescription('When TRUE, this entry is used, when FALSE, this entry is skipped when filtering.')
taclProfile_PermitList_SourceAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1, 4), IpAddress()).setLabel("taclProfile-PermitList-SourceAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: taclProfile_PermitList_SourceAddress.setStatus('mandatory')
if mibBuilder.loadTexts: taclProfile_PermitList_SourceAddress.setDescription('A value to compare with the masked source addresses.')
taclProfile_PermitList_SourceAddressMask = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1, 5), IpAddress()).setLabel("taclProfile-PermitList-SourceAddressMask").setMaxAccess("readwrite")
if mibBuilder.loadTexts: taclProfile_PermitList_SourceAddressMask.setStatus('mandatory')
if mibBuilder.loadTexts: taclProfile_PermitList_SourceAddressMask.setDescription('A mask to apply to a source address before comparison.')
mibBuilder.exportSymbols("ASCEND-MIBTACL-MIB", taclProfile_PermitList_SourceAddress=taclProfile_PermitList_SourceAddress, mibtaclProfile_PermitListEntry=mibtaclProfile_PermitListEntry, taclProfile_PermitList_Index_o=taclProfile_PermitList_Index_o, mibtaclProfileTable=mibtaclProfileTable, mibtaclProfile=mibtaclProfile, taclProfile_PermitList_ValidEntry=taclProfile_PermitList_ValidEntry, taclProfile_Action_o=taclProfile_Action_o, taclProfile_EnablePermit=taclProfile_EnablePermit, taclProfile_PermitList_SourceAddressMask=taclProfile_PermitList_SourceAddressMask, taclProfile_PermitList_Index1_o=taclProfile_PermitList_Index1_o, mibtaclProfile_PermitListTable=mibtaclProfile_PermitListTable, DisplayString=DisplayString, mibtaclProfileEntry=mibtaclProfileEntry, taclProfile_Index_o=taclProfile_Index_o)
