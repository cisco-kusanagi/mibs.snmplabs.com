#
# PySNMP MIB module RSPAN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RSPAN-MGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:50:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, Counter64, Bits, ModuleIdentity, ObjectIdentity, IpAddress, NotificationType, Unsigned32, Gauge32, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Counter64", "Bits", "ModuleIdentity", "ObjectIdentity", "IpAddress", "NotificationType", "Unsigned32", "Gauge32", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

swRSPANMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 68))
if mibBuilder.loadTexts: swRSPANMIB.setLastUpdated('200807290000Z')
if mibBuilder.loadTexts: swRSPANMIB.setOrganization('D-Link Crop.')
swRSPANCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 68, 1))
swRSPANInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 68, 2))
swRSPANMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 68, 3))
swRSPANState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 68, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swRSPANState.setStatus('current')
swRSPANMaxSupportedEntry = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 68, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRSPANMaxSupportedEntry.setStatus('current')
swRSPANCurrentNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 68, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRSPANCurrentNumEntries.setStatus('current')
swRSPANTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1), )
if mibBuilder.loadTexts: swRSPANTable.setStatus('current')
swRSPANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1), ).setIndexNames((0, "RSPAN-MGMT-MIB", "swRSPANVLANID"))
if mibBuilder.loadTexts: swRSPANEntry.setStatus('current')
swRSPANVLANID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swRSPANVLANID.setStatus('current')
swRSPANSourceIngress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1, 2), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swRSPANSourceIngress.setStatus('current')
swRSPANSourceEgress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1, 3), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swRSPANSourceEgress.setStatus('current')
swRSPANRedirct = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1, 4), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swRSPANRedirct.setStatus('current')
swRSPANRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swRSPANRowStatus.setStatus('current')
mibBuilder.exportSymbols("RSPAN-MGMT-MIB", swRSPANTable=swRSPANTable, PortList=PortList, swRSPANInfo=swRSPANInfo, swRSPANSourceIngress=swRSPANSourceIngress, swRSPANSourceEgress=swRSPANSourceEgress, swRSPANRedirct=swRSPANRedirct, swRSPANMIB=swRSPANMIB, swRSPANEntry=swRSPANEntry, VlanId=VlanId, swRSPANMaxSupportedEntry=swRSPANMaxSupportedEntry, swRSPANState=swRSPANState, swRSPANRowStatus=swRSPANRowStatus, swRSPANVLANID=swRSPANVLANID, swRSPANCurrentNumEntries=swRSPANCurrentNumEntries, swRSPANCtrl=swRSPANCtrl, PYSNMP_MODULE_ID=swRSPANMIB, swRSPANMgmt=swRSPANMgmt)
