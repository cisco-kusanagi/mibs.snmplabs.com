#
# PySNMP MIB module AXIS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AXIS-ROOT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:33:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, iso, Unsigned32, Gauge32, ObjectIdentity, ModuleIdentity, IpAddress, Counter64, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "iso", "Unsigned32", "Gauge32", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Counter64", "Integer32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
axis = ModuleIdentity((1, 3, 6, 1, 4, 1, 368))
axis.setRevisions(('2012-06-08 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: axis.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: axis.setLastUpdated('201206081000Z')
if mibBuilder.loadTexts: axis.setOrganization('Axis Communications AB')
if mibBuilder.loadTexts: axis.setContactInfo('Postal: Axis Communications AB Emdalavagen 14 SE-223 69 Lund Sweden Phone: +46 (0)46 272 18 00 Fax: +46 (0)46 13 61 30 E-Mail: info@axis.com Web: www.axis.com')
if mibBuilder.loadTexts: axis.setDescription('The AXIS root MIB.')
products = ObjectIdentity((1, 3, 6, 1, 4, 1, 368, 1))
if mibBuilder.loadTexts: products.setStatus('current')
if mibBuilder.loadTexts: products.setDescription('products is the root OBJECT IDENTIFIER from which sysObjectID values are assigned. Actual values and respectively products sub-tree are defined in: AXIS-PRINTSERVER-MIB AXIS-VIDEO-MIB')
mibBuilder.exportSymbols("AXIS-ROOT-MIB", PYSNMP_MODULE_ID=axis, axis=axis, products=products)
