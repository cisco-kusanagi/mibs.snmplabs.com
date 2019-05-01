#
# PySNMP MIB module PGP-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PGP-SMI
# Produced by pysmi-0.3.4 at Wed May  1 14:40:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, enterprises, Counter64, Unsigned32, MibIdentifier, ModuleIdentity, Bits, Gauge32, Counter32, TimeTicks, NotificationType, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "enterprises", "Counter64", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Bits", "Gauge32", "Counter32", "TimeTicks", "NotificationType", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pgp = ModuleIdentity((1, 3, 6, 1, 4, 1, 17766))
pgp.setRevisions(('2004-12-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pgp.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: pgp.setLastUpdated('200412080000Z')
if mibBuilder.loadTexts: pgp.setOrganization('PGP Corporation')
if mibBuilder.loadTexts: pgp.setContactInfo(' PGP Corporation Internet: http://www.pgp.com')
if mibBuilder.loadTexts: pgp.setDescription('The Structure of Management Information for PGP Corporation.')
products = ObjectIdentity((1, 3, 6, 1, 4, 1, 17766, 1))
if mibBuilder.loadTexts: products.setStatus('current')
if mibBuilder.loadTexts: products.setDescription('products is the root OID from which subtrees for each PGP product are allocated.')
mibBuilder.exportSymbols("PGP-SMI", pgp=pgp, products=products, PYSNMP_MODULE_ID=pgp)
