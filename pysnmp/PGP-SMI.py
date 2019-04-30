#
# PySNMP MIB module PGP-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PGP-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 20:31:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, enterprises, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, Bits, TimeTicks, IpAddress, MibIdentifier, Integer32, ModuleIdentity, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "enterprises", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "Bits", "TimeTicks", "IpAddress", "MibIdentifier", "Integer32", "ModuleIdentity", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pgp = ModuleIdentity((1, 3, 6, 1, 4, 1, 17766))
pgp.setRevisions(('2004-12-08 00:00',))
if mibBuilder.loadTexts: pgp.setLastUpdated('200412080000Z')
if mibBuilder.loadTexts: pgp.setOrganization('PGP Corporation')
products = ObjectIdentity((1, 3, 6, 1, 4, 1, 17766, 1))
if mibBuilder.loadTexts: products.setStatus('current')
mibBuilder.exportSymbols("PGP-SMI", PYSNMP_MODULE_ID=pgp, products=products, pgp=pgp)
