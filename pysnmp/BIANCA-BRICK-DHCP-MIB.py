#
# PySNMP MIB module BIANCA-BRICK-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-BRICK-DHCP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:21:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Bits, TimeTicks, Gauge32, ModuleIdentity, Unsigned32, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, Counter32, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "TimeTicks", "Gauge32", "ModuleIdentity", "Unsigned32", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "Counter32", "Counter64", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
biboip = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 5))
class PhysAddress(OctetString):
    pass

class Date(Integer32):
    pass

ipDhcpTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 5, 8), )
if mibBuilder.loadTexts: ipDhcpTable.setStatus('mandatory')
ipDhcpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1), ).setIndexNames((0, "BIANCA-BRICK-DHCP-MIB", "ipDhcpIfIndex"))
if mibBuilder.loadTexts: ipDhcpEntry.setStatus('mandatory')
ipDhcpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipDhcpIfIndex.setStatus('mandatory')
ipDhcpState = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipDhcpState.setStatus('mandatory')
ipDhcpFirst = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipDhcpFirst.setStatus('mandatory')
ipDhcpRange = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipDhcpRange.setStatus('mandatory')
ipDhcpLease = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipDhcpLease.setStatus('mandatory')
ipDhcpPhys = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1, 6), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipDhcpPhys.setStatus('mandatory')
ipDhcpNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("bnode", 2), ("pnode", 3), ("mnode", 4), ("hnode", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipDhcpNodeType.setStatus('mandatory')
ipDhcpGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 8, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipDhcpGateway.setStatus('mandatory')
ipDhcpInUseTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 5, 9), )
if mibBuilder.loadTexts: ipDhcpInUseTable.setStatus('mandatory')
ipDhcpInUseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 5, 9, 1), ).setIndexNames((0, "BIANCA-BRICK-DHCP-MIB", "ipDhcpInUseAddress"))
if mibBuilder.loadTexts: ipDhcpInUseEntry.setStatus('mandatory')
ipDhcpInUseAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 9, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDhcpInUseAddress.setStatus('mandatory')
ipDhcpInUsePhys = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 9, 1, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDhcpInUsePhys.setStatus('mandatory')
ipDhcpInUseExpires = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 5, 9, 1, 3), Date()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDhcpInUseExpires.setStatus('mandatory')
mibBuilder.exportSymbols("BIANCA-BRICK-DHCP-MIB", ipDhcpInUseExpires=ipDhcpInUseExpires, bibo=bibo, private=private, ipDhcpLease=ipDhcpLease, PhysAddress=PhysAddress, ipDhcpInUseEntry=ipDhcpInUseEntry, ipDhcpInUsePhys=ipDhcpInUsePhys, Date=Date, ipDhcpRange=ipDhcpRange, ipDhcpInUseAddress=ipDhcpInUseAddress, org=org, bintec=bintec, ipDhcpState=ipDhcpState, enterprises=enterprises, ipDhcpPhys=ipDhcpPhys, ipDhcpNodeType=ipDhcpNodeType, internet=internet, dod=dod, ipDhcpIfIndex=ipDhcpIfIndex, ipDhcpInUseTable=ipDhcpInUseTable, ipDhcpFirst=ipDhcpFirst, ipDhcpTable=ipDhcpTable, ipDhcpEntry=ipDhcpEntry, biboip=biboip, ipDhcpGateway=ipDhcpGateway)
