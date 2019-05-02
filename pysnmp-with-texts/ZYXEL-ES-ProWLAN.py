#
# PySNMP MIB module ZYXEL-ES-ProWLAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-ES-ProWLAN
# Produced by pysmi-0.3.4 at Wed May  1 15:49:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter64, NotificationType, ObjectIdentity, Bits, Integer32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, Unsigned32, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "NotificationType", "ObjectIdentity", "Bits", "Integer32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "Unsigned32", "Gauge32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esProductSpecific, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esProductSpecific")
esProWLAN = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 1))
if mibBuilder.loadTexts: esProWLAN.setLastUpdated('201010060000Z')
if mibBuilder.loadTexts: esProWLAN.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: esProWLAN.setContactInfo('')
if mibBuilder.loadTexts: esProWLAN.setDescription('The subtree for ProWLAN product line')
mibBuilder.exportSymbols("ZYXEL-ES-ProWLAN", PYSNMP_MODULE_ID=esProWLAN, esProWLAN=esProWLAN)
