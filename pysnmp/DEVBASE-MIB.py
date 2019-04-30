#
# PySNMP MIB module DEVBASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DEVBASE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:26:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibIdentifier, Gauge32, ObjectIdentity, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, iso, Counter32, Bits, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Gauge32", "ObjectIdentity", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "iso", "Counter32", "Bits", "Counter64", "ModuleIdentity")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
aniDevBase = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 2, 1))
if mibBuilder.loadTexts: aniDevBase.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniDevBase.setOrganization('Aperto Networks')
aniDevProductName = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevProductName.setStatus('current')
aniDevLanIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevLanIpAddr.setStatus('current')
aniDevLanSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevLanSubnetMask.setStatus('current')
aniDevDefaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevDefaultGateway.setStatus('current')
aniDevMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevMacAddr.setStatus('current')
mibBuilder.exportSymbols("DEVBASE-MIB", aniDevDefaultGateway=aniDevDefaultGateway, aniDevBase=aniDevBase, aniDevLanIpAddr=aniDevLanIpAddr, aniDevProductName=aniDevProductName, aniDevLanSubnetMask=aniDevLanSubnetMask, PYSNMP_MODULE_ID=aniDevBase, aniDevMacAddr=aniDevMacAddr)
