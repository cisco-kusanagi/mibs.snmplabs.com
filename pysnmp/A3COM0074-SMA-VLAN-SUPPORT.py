#
# PySNMP MIB module A3COM0074-SMA-VLAN-SUPPORT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM0074-SMA-VLAN-SUPPORT
# Produced by pysmi-0.3.4 at Mon Apr 29 16:54:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
smaVlanSupport, = mibBuilder.importSymbols("A3COM0004-GENERIC", "smaVlanSupport")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
a3ComVlanIfIndex, = mibBuilder.importSymbols("GENERIC-3COM-VLAN-MIB-1-0-7", "a3ComVlanIfIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, iso, Gauge32, Integer32, IpAddress, TimeTicks, Bits, Unsigned32, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "iso", "Gauge32", "Integer32", "IpAddress", "TimeTicks", "Bits", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
a3ComVlanPrivateIfTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 35, 1), )
if mibBuilder.loadTexts: a3ComVlanPrivateIfTable.setStatus('mandatory')
a3ComVlanPrivateIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 35, 1, 1), ).setIndexNames((0, "GENERIC-3COM-VLAN-MIB-1-0-7", "a3ComVlanIfIndex"))
if mibBuilder.loadTexts: a3ComVlanPrivateIfEntry.setStatus('mandatory')
a3ComVlanCreateType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 35, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("automatic", 1), ("dynamic", 2), ("manual", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanCreateType.setStatus('mandatory')
a3ComVlanMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 35, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComVlanMembers.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM0074-SMA-VLAN-SUPPORT", a3ComVlanMembers=a3ComVlanMembers, a3ComVlanPrivateIfEntry=a3ComVlanPrivateIfEntry, a3ComVlanPrivateIfTable=a3ComVlanPrivateIfTable, a3ComVlanCreateType=a3ComVlanCreateType)
