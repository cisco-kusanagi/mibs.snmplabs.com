#
# PySNMP MIB module NMS-L2-PROTOCOL-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-L2-PROTOCOL-TUNNEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:12:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
nmsMgmt, = mibBuilder.importSymbols("NMS-SMI", "nmsMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter32, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, ObjectIdentity, ModuleIdentity, IpAddress, NotificationType, Counter64, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "ObjectIdentity", "ModuleIdentity", "IpAddress", "NotificationType", "Counter64", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nmsL2ProtocolTunnelMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11606, 10, 9, 357))
if mibBuilder.loadTexts: nmsL2ProtocolTunnelMIB.setLastUpdated('201302210000Z')
if mibBuilder.loadTexts: nmsL2ProtocolTunnelMIB.setOrganization('')
l2ptMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 9, 357, 1))
l2ptGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 9, 357, 1, 1))
l2ptIntfTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 9, 357, 1, 2), )
if mibBuilder.loadTexts: l2ptIntfTable.setStatus('current')
l2ptIntfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 9, 357, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: l2ptIntfEntry.setStatus('current')
l2ptIntfStpTnl = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 9, 357, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2ptIntfStpTnl.setStatus('current')
mibBuilder.exportSymbols("NMS-L2-PROTOCOL-TUNNEL-MIB", PYSNMP_MODULE_ID=nmsL2ProtocolTunnelMIB, l2ptIntfTable=l2ptIntfTable, nmsL2ProtocolTunnelMIB=nmsL2ProtocolTunnelMIB, l2ptIntfStpTnl=l2ptIntfStpTnl, l2ptMIBObjects=l2ptMIBObjects, l2ptIntfEntry=l2ptIntfEntry, l2ptGlobal=l2ptGlobal)
