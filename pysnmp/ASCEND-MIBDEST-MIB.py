#
# PySNMP MIB module ASCEND-MIBDEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBDEST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, Integer32, TimeTicks, Gauge32, Unsigned32, iso, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "Integer32", "TimeTicks", "Gauge32", "Unsigned32", "iso", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibdestProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 73))
mibdestProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 73, 1), )
if mibBuilder.loadTexts: mibdestProfileTable.setStatus('mandatory')
mibdestProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 73, 1, 1), ).setIndexNames((0, "ASCEND-MIBDEST-MIB", "destProfile-PlanNumber"))
if mibBuilder.loadTexts: mibdestProfileEntry.setStatus('mandatory')
destProfile_PlanNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 73, 1, 1, 1), Integer32()).setLabel("destProfile-PlanNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: destProfile_PlanNumber.setStatus('mandatory')
destProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 73, 1, 1, 2), DisplayString()).setLabel("destProfile-Name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: destProfile_Name.setStatus('mandatory')
destProfile_NumberOption = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 73, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("destSelFirstAvail", 1), ("destSelFirstActive", 2), ("destSelAnyAvail", 3), ("numberOfDestSel", 4)))).setLabel("destProfile-NumberOption").setMaxAccess("readwrite")
if mibBuilder.loadTexts: destProfile_NumberOption.setStatus('mandatory')
destProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 73, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("destProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: destProfile_Action_o.setStatus('mandatory')
mibdestProfile_DestNumberTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 73, 2), ).setLabel("mibdestProfile-DestNumberTable")
if mibBuilder.loadTexts: mibdestProfile_DestNumberTable.setStatus('mandatory')
mibdestProfile_DestNumberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 73, 2, 1), ).setLabel("mibdestProfile-DestNumberEntry").setIndexNames((0, "ASCEND-MIBDEST-MIB", "destProfile-DestNumber-PlanNumber"), (0, "ASCEND-MIBDEST-MIB", "destProfile-DestNumber-Index-o"))
if mibBuilder.loadTexts: mibdestProfile_DestNumberEntry.setStatus('mandatory')
destProfile_DestNumber_PlanNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 73, 2, 1, 1), Integer32()).setLabel("destProfile-DestNumber-PlanNumber").setMaxAccess("readonly")
if mibBuilder.loadTexts: destProfile_DestNumber_PlanNumber.setStatus('mandatory')
destProfile_DestNumber_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 73, 2, 1, 2), Integer32()).setLabel("destProfile-DestNumber-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: destProfile_DestNumber_Index_o.setStatus('mandatory')
destProfile_DestNumber_PhoneNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 73, 2, 1, 3), DisplayString()).setLabel("destProfile-DestNumber-PhoneNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: destProfile_DestNumber_PhoneNumber.setStatus('mandatory')
destProfile_DestNumber_CallByCallId = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 73, 2, 1, 4), Integer32()).setLabel("destProfile-DestNumber-CallByCallId").setMaxAccess("readwrite")
if mibBuilder.loadTexts: destProfile_DestNumber_CallByCallId.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBDEST-MIB", destProfile_Name=destProfile_Name, destProfile_Action_o=destProfile_Action_o, mibdestProfile_DestNumberTable=mibdestProfile_DestNumberTable, mibdestProfile_DestNumberEntry=mibdestProfile_DestNumberEntry, DisplayString=DisplayString, mibdestProfileEntry=mibdestProfileEntry, destProfile_NumberOption=destProfile_NumberOption, mibdestProfile=mibdestProfile, destProfile_PlanNumber=destProfile_PlanNumber, destProfile_DestNumber_PhoneNumber=destProfile_DestNumber_PhoneNumber, destProfile_DestNumber_CallByCallId=destProfile_DestNumber_CallByCallId, mibdestProfileTable=mibdestProfileTable, destProfile_DestNumber_Index_o=destProfile_DestNumber_Index_o, destProfile_DestNumber_PlanNumber=destProfile_DestNumber_PlanNumber)
