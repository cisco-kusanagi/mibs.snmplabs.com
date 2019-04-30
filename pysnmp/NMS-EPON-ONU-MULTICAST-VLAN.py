#
# PySNMP MIB module NMS-EPON-ONU-MULTICAST-VLAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-EPON-ONU-MULTICAST-VLAN
# Produced by pysmi-0.3.4 at Mon Apr 29 20:12:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, IpAddress, Counter32, Gauge32, MibIdentifier, ModuleIdentity, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, ObjectIdentity, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "Counter32", "Gauge32", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "ObjectIdentity", "Bits", "NotificationType")
DisplayString, TruthValue, PhysAddress, MacAddress, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "PhysAddress", "MacAddress", "TextualConvention", "RowStatus")
nmsEponOnuMulticastVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 101, 14))
nmsepononumulticastvlanTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 101, 14, 1), )
if mibBuilder.loadTexts: nmsepononumulticastvlanTable.setStatus('mandatory')
nmsEponOnuVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 101, 14, 1, 1), ).setIndexNames((0, "NMS-EPON-ONU-MULTICAST-VLAN", "onuLlidDiid"), (0, "NMS-EPON-ONU-MULTICAST-VLAN", "onuIfSequenceNo"), (0, "NMS-EPON-ONU-MULTICAST-VLAN", "onuMcstMcVlanID"))
if mibBuilder.loadTexts: nmsEponOnuVlanEntry.setStatus('mandatory')
onuLlidDiid = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 14, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: onuLlidDiid.setStatus('mandatory')
onuIfSequenceNo = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 14, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: onuIfSequenceNo.setStatus('mandatory')
onuMcstMcVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 14, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: onuMcstMcVlanID.setStatus('mandatory')
onuMcVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 14, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: onuMcVlanRowStatus.setStatus('mandatory')
mibBuilder.exportSymbols("NMS-EPON-ONU-MULTICAST-VLAN", onuMcstMcVlanID=onuMcstMcVlanID, nmsepononumulticastvlanTable=nmsepononumulticastvlanTable, onuMcVlanRowStatus=onuMcVlanRowStatus, onuIfSequenceNo=onuIfSequenceNo, nmsEponOnuMulticastVlan=nmsEponOnuMulticastVlan, nmsEponOnuVlanEntry=nmsEponOnuVlanEntry, onuLlidDiid=onuLlidDiid)
