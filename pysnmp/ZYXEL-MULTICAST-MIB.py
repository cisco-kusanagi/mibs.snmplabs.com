#
# PySNMP MIB module ZYXEL-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-MULTICAST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:44:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Counter64, Gauge32, MibIdentifier, iso, Counter32, ObjectIdentity, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Counter64", "Gauge32", "MibIdentifier", "iso", "Counter32", "ObjectIdentity", "IpAddress", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelMulticast = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54))
if mibBuilder.loadTexts: zyxelMulticast.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelMulticast.setOrganization('Enterprise Solution ZyXEL')
zyxelMulticastSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1))
zyMulticastUnknownMulticastFrameForwarding = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("flooding", 1), ("drop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMulticastUnknownMulticastFrameForwarding.setStatus('current')
zyMulticastReservedMulticastFrameForwarding = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("flooding", 1), ("drop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMulticastReservedMulticastFrameForwarding.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-MULTICAST-MIB", PYSNMP_MODULE_ID=zyxelMulticast, zyMulticastUnknownMulticastFrameForwarding=zyMulticastUnknownMulticastFrameForwarding, zyxelMulticastSetup=zyxelMulticastSetup, zyxelMulticast=zyxelMulticast, zyMulticastReservedMulticastFrameForwarding=zyMulticastReservedMulticastFrameForwarding)
