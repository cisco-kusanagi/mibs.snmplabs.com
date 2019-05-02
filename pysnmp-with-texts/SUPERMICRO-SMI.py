#
# PySNMP MIB module SUPERMICRO-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SUPERMICRO-SMI
# Produced by pysmi-0.3.4 at Wed May  1 15:12:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, MibIdentifier, Gauge32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Unsigned32, NotificationType, enterprises, Counter32, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Gauge32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Unsigned32", "NotificationType", "enterprises", "Counter32", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
supermicro = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876))
supermicro.setRevisions(('2001-10-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: supermicro.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: supermicro.setLastUpdated('200110260000Z')
if mibBuilder.loadTexts: supermicro.setOrganization('Super Micro Computer Inc.')
if mibBuilder.loadTexts: supermicro.setContactInfo(' Software Lab Postal: 980 Rock Avenue San Jose, CA 95131 USA Tel: +1 408 503 8000 E-mail: SoftLab@supermicro.com')
if mibBuilder.loadTexts: supermicro.setDescription('The Structure of Management Information for the Super Micro enterprise.')
smProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 10876, 1))
if mibBuilder.loadTexts: smProducts.setStatus('current')
if mibBuilder.loadTexts: smProducts.setDescription('smProducts is the root OBJECT IDENTIFIER from which sysObjectID values are assigned. Actual values are defined in SUPERMICRO-PRODUCTS-MIB.')
smHealth = ObjectIdentity((1, 3, 6, 1, 4, 1, 10876, 2))
if mibBuilder.loadTexts: smHealth.setStatus('current')
if mibBuilder.loadTexts: smHealth.setDescription('smHealth is the main subtree for new mib development.')
mibBuilder.exportSymbols("SUPERMICRO-SMI", PYSNMP_MODULE_ID=supermicro, supermicro=supermicro, smHealth=smHealth, smProducts=smProducts)
