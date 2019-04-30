#
# PySNMP MIB module ZYXEL-ES-ProWLAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-ES-ProWLAN
# Produced by pysmi-0.3.4 at Mon Apr 29 21:43:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, Counter32, MibIdentifier, IpAddress, Integer32, Bits, NotificationType, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Counter32", "MibIdentifier", "IpAddress", "Integer32", "Bits", "NotificationType", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esProductSpecific, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esProductSpecific")
esProWLAN = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 1))
if mibBuilder.loadTexts: esProWLAN.setLastUpdated('201010060000Z')
if mibBuilder.loadTexts: esProWLAN.setOrganization('Enterprise Solution ZyXEL')
mibBuilder.exportSymbols("ZYXEL-ES-ProWLAN", PYSNMP_MODULE_ID=esProWLAN, esProWLAN=esProWLAN)
