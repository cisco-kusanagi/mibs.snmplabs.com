#
# PySNMP MIB module SUN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SUN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:12:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, ObjectIdentity, Counter32, TimeTicks, Unsigned32, enterprises, MibIdentifier, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "ObjectIdentity", "Counter32", "TimeTicks", "Unsigned32", "enterprises", "MibIdentifier", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Bits", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sunMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 42))
if mibBuilder.loadTexts: sunMIB.setLastUpdated('200309180000Z')
if mibBuilder.loadTexts: sunMIB.setOrganization('Sun Microsystems, Inc.')
if mibBuilder.loadTexts: sunMIB.setContactInfo('Customer support')
if mibBuilder.loadTexts: sunMIB.setDescription('MIB that defines the Sun enterprise ')
sun = MibIdentifier((1, 3, 6, 1, 4, 1, 42))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2))
management = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 2))
sma = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 2, 4))
mibBuilder.exportSymbols("SUN-MIB", sma=sma, sun=sun, PYSNMP_MODULE_ID=sunMIB, sunMIB=sunMIB, management=management, products=products)
