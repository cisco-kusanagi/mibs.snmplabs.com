#
# PySNMP MIB module ASCEND-MIBTACL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBTACL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, TimeTicks, Integer32, MibIdentifier, iso, Counter32, IpAddress, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "TimeTicks", "Integer32", "MibIdentifier", "iso", "Counter32", "IpAddress", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibtaclProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 128))
mibtaclProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 128, 1), )
if mibBuilder.loadTexts: mibtaclProfileTable.setStatus('mandatory')
mibtaclProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 128, 1, 1), ).setIndexNames((0, "ASCEND-MIBTACL-MIB", "taclProfile-Index-o"))
if mibBuilder.loadTexts: mibtaclProfileEntry.setStatus('mandatory')
taclProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 128, 1, 1, 1), Integer32()).setLabel("taclProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: taclProfile_Index_o.setStatus('mandatory')
taclProfile_EnablePermit = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 128, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("taclProfile-EnablePermit").setMaxAccess("readwrite")
if mibBuilder.loadTexts: taclProfile_EnablePermit.setStatus('mandatory')
taclProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 128, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("taclProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: taclProfile_Action_o.setStatus('mandatory')
mibtaclProfile_PermitListTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 128, 2), ).setLabel("mibtaclProfile-PermitListTable")
if mibBuilder.loadTexts: mibtaclProfile_PermitListTable.setStatus('mandatory')
mibtaclProfile_PermitListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1), ).setLabel("mibtaclProfile-PermitListEntry").setIndexNames((0, "ASCEND-MIBTACL-MIB", "taclProfile-PermitList-Index-o"), (0, "ASCEND-MIBTACL-MIB", "taclProfile-PermitList-Index1-o"))
if mibBuilder.loadTexts: mibtaclProfile_PermitListEntry.setStatus('mandatory')
taclProfile_PermitList_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1, 1), Integer32()).setLabel("taclProfile-PermitList-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: taclProfile_PermitList_Index_o.setStatus('mandatory')
taclProfile_PermitList_Index1_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1, 2), Integer32()).setLabel("taclProfile-PermitList-Index1-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: taclProfile_PermitList_Index1_o.setStatus('mandatory')
taclProfile_PermitList_ValidEntry = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("taclProfile-PermitList-ValidEntry").setMaxAccess("readwrite")
if mibBuilder.loadTexts: taclProfile_PermitList_ValidEntry.setStatus('mandatory')
taclProfile_PermitList_SourceAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1, 4), IpAddress()).setLabel("taclProfile-PermitList-SourceAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: taclProfile_PermitList_SourceAddress.setStatus('mandatory')
taclProfile_PermitList_SourceAddressMask = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1, 5), IpAddress()).setLabel("taclProfile-PermitList-SourceAddressMask").setMaxAccess("readwrite")
if mibBuilder.loadTexts: taclProfile_PermitList_SourceAddressMask.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBTACL-MIB", taclProfile_EnablePermit=taclProfile_EnablePermit, mibtaclProfile_PermitListTable=mibtaclProfile_PermitListTable, mibtaclProfileTable=mibtaclProfileTable, mibtaclProfile_PermitListEntry=mibtaclProfile_PermitListEntry, taclProfile_PermitList_Index_o=taclProfile_PermitList_Index_o, taclProfile_PermitList_ValidEntry=taclProfile_PermitList_ValidEntry, taclProfile_Index_o=taclProfile_Index_o, taclProfile_PermitList_SourceAddressMask=taclProfile_PermitList_SourceAddressMask, DisplayString=DisplayString, mibtaclProfile=mibtaclProfile, taclProfile_PermitList_SourceAddress=taclProfile_PermitList_SourceAddress, taclProfile_PermitList_Index1_o=taclProfile_PermitList_Index1_o, mibtaclProfileEntry=mibtaclProfileEntry, taclProfile_Action_o=taclProfile_Action_o)
