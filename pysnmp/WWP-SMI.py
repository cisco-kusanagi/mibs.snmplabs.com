#
# PySNMP MIB module WWP-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 21:30:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, NotificationType, ModuleIdentity, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, iso, Counter64, Integer32, MibIdentifier, enterprises, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "iso", "Counter64", "Integer32", "MibIdentifier", "enterprises", "Counter32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wwp = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141))
wwp.setRevisions(('2013-02-09 01:36',))
if mibBuilder.loadTexts: wwp.setLastUpdated('201302090136Z')
if mibBuilder.loadTexts: wwp.setOrganization('Ciena, Inc.')
wwpProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 6141, 1))
if mibBuilder.loadTexts: wwpProducts.setStatus('current')
wwpModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 6141, 2))
if mibBuilder.loadTexts: wwpModules.setStatus('current')
wwpModulesLeos = ObjectIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 60))
if mibBuilder.loadTexts: wwpModulesLeos.setStatus('current')
wwpModulesLeosTce = ObjectIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 61))
if mibBuilder.loadTexts: wwpModulesLeosTce.setStatus('current')
mibBuilder.exportSymbols("WWP-SMI", wwpModules=wwpModules, wwpModulesLeos=wwpModulesLeos, wwp=wwp, PYSNMP_MODULE_ID=wwp, wwpModulesLeosTce=wwpModulesLeosTce, wwpProducts=wwpProducts)
