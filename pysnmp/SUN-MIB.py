#
# PySNMP MIB module SUN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SUN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:04:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Integer32, NotificationType, Unsigned32, Bits, TimeTicks, Counter64, ObjectIdentity, IpAddress, enterprises, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Integer32", "NotificationType", "Unsigned32", "Bits", "TimeTicks", "Counter64", "ObjectIdentity", "IpAddress", "enterprises", "ModuleIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sunMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 42))
if mibBuilder.loadTexts: sunMIB.setLastUpdated('200309180000Z')
if mibBuilder.loadTexts: sunMIB.setOrganization('Sun Microsystems, Inc.')
sun = MibIdentifier((1, 3, 6, 1, 4, 1, 42))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2))
management = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 2))
sma = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 2, 4))
mibBuilder.exportSymbols("SUN-MIB", products=products, management=management, sma=sma, sunMIB=sunMIB, PYSNMP_MODULE_ID=sunMIB, sun=sun)
