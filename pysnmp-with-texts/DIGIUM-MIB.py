#
# PySNMP MIB module DIGIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DIGIUM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:29:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, MibIdentifier, Counter32, Counter64, Unsigned32, Bits, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, enterprises, IpAddress, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "MibIdentifier", "Counter32", "Counter64", "Unsigned32", "Bits", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "enterprises", "IpAddress", "Integer32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
digium = ModuleIdentity((1, 3, 6, 1, 4, 1, 22736))
if mibBuilder.loadTexts: digium.setLastUpdated('200602041900Z')
if mibBuilder.loadTexts: digium.setOrganization('Digium, Inc.')
if mibBuilder.loadTexts: digium.setContactInfo('Mark Spencer Email: markster@digium.com')
if mibBuilder.loadTexts: digium.setDescription('')
mibBuilder.exportSymbols("DIGIUM-MIB", PYSNMP_MODULE_ID=digium, digium=digium)
