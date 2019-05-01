#
# PySNMP MIB module WWP-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-SMI
# Produced by pysmi-0.3.4 at Wed May  1 15:37:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ObjectIdentity, Bits, TimeTicks, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Integer32, MibIdentifier, ModuleIdentity, enterprises, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "Bits", "TimeTicks", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Integer32", "MibIdentifier", "ModuleIdentity", "enterprises", "IpAddress", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wwp = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141))
wwp.setRevisions(('2013-02-09 01:36',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wwp.setRevisionsDescriptions(('MIB Version: 04-10-01-0027',))
if mibBuilder.loadTexts: wwp.setLastUpdated('201302090136Z')
if mibBuilder.loadTexts: wwp.setOrganization('Ciena, Inc.')
if mibBuilder.loadTexts: wwp.setContactInfo(' Mib Meister 115 North Sullivan Road Spokane Valley, WA 99037 USA Phone: +1 509 242 9000 Email: support@ciena.com')
if mibBuilder.loadTexts: wwp.setDescription('Top-level WWP node definitions.')
wwpProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 6141, 1))
if mibBuilder.loadTexts: wwpProducts.setStatus('current')
if mibBuilder.loadTexts: wwpProducts.setDescription('wwpProducts is the root OBJECT-IDENTIFIER for all WWP products. sysObjectID values will be assigned the OID representing the product specified in WWP-PRODUCTS-MIB.my.')
wwpModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 6141, 2))
if mibBuilder.loadTexts: wwpModules.setStatus('current')
if mibBuilder.loadTexts: wwpModules.setDescription('wwpModules provides a root object identifier that can be used to assign MODULE-IDENTIFY values.')
wwpModulesLeos = ObjectIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 60))
if mibBuilder.loadTexts: wwpModulesLeos.setStatus('current')
if mibBuilder.loadTexts: wwpModulesLeos.setDescription('wwpModulesLeos provides a root object identifier for leos that can be used to assign MODULE-IDENTIFY values.')
wwpModulesLeosTce = ObjectIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 61))
if mibBuilder.loadTexts: wwpModulesLeosTce.setStatus('current')
if mibBuilder.loadTexts: wwpModulesLeosTce.setDescription('wwpModulesLeosTce provides a root object identifier for leos TCE that can be used to assign MODULE-IDENTIFY values.')
mibBuilder.exportSymbols("WWP-SMI", wwpModules=wwpModules, wwpProducts=wwpProducts, PYSNMP_MODULE_ID=wwp, wwp=wwp, wwpModulesLeosTce=wwpModulesLeosTce, wwpModulesLeos=wwpModulesLeos)
