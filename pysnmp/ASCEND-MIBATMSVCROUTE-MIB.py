#
# PySNMP MIB module ASCEND-MIBATMSVCROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBATMSVCROUTE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, ModuleIdentity, Integer32, Unsigned32, NotificationType, Bits, iso, TimeTicks, Gauge32, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "ModuleIdentity", "Integer32", "Unsigned32", "NotificationType", "Bits", "iso", "TimeTicks", "Gauge32", "IpAddress", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibatmSvcRouteProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 55))
mibatmSvcRouteProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 55, 1), )
if mibBuilder.loadTexts: mibatmSvcRouteProfileTable.setStatus('mandatory')
mibatmSvcRouteProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1), ).setIndexNames((0, "ASCEND-MIBATMSVCROUTE-MIB", "atmSvcRouteProfile-Name"))
if mibBuilder.loadTexts: mibatmSvcRouteProfileEntry.setStatus('mandatory')
atmSvcRouteProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1, 1), DisplayString()).setLabel("atmSvcRouteProfile-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSvcRouteProfile_Name.setStatus('mandatory')
atmSvcRouteProfile_Active = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("atmSvcRouteProfile-Active").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSvcRouteProfile_Active.setStatus('mandatory')
atmSvcRouteProfile_AddressPrefix = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1, 3), DisplayString()).setLabel("atmSvcRouteProfile-AddressPrefix").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSvcRouteProfile_AddressPrefix.setStatus('mandatory')
atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("atmSvcRouteProfile-InterfaceAddress-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Shelf.setStatus('mandatory')
atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("atmSvcRouteProfile-InterfaceAddress-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Slot.setStatus('mandatory')
atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1, 6), Integer32()).setLabel("atmSvcRouteProfile-InterfaceAddress-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setStatus('mandatory')
atmSvcRouteProfile_InterfaceAddress_LogicalItem = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1, 7), Integer32()).setLabel("atmSvcRouteProfile-InterfaceAddress-LogicalItem").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSvcRouteProfile_InterfaceAddress_LogicalItem.setStatus('mandatory')
atmSvcRouteProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("atmSvcRouteProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSvcRouteProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBATMSVCROUTE-MIB", mibatmSvcRouteProfileTable=mibatmSvcRouteProfileTable, atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_ItemNumber=atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_ItemNumber, atmSvcRouteProfile_Name=atmSvcRouteProfile_Name, DisplayString=DisplayString, atmSvcRouteProfile_Action_o=atmSvcRouteProfile_Action_o, mibatmSvcRouteProfileEntry=mibatmSvcRouteProfileEntry, atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Shelf=atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Shelf, mibatmSvcRouteProfile=mibatmSvcRouteProfile, atmSvcRouteProfile_AddressPrefix=atmSvcRouteProfile_AddressPrefix, atmSvcRouteProfile_Active=atmSvcRouteProfile_Active, atmSvcRouteProfile_InterfaceAddress_LogicalItem=atmSvcRouteProfile_InterfaceAddress_LogicalItem, atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Slot=atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Slot)
