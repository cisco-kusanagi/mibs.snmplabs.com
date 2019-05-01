#
# PySNMP MIB module ATTO-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATTO-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:31:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, NotificationType, ObjectIdentity, Bits, Counter64, ModuleIdentity, Integer32, iso, enterprises, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "NotificationType", "ObjectIdentity", "Bits", "Counter64", "ModuleIdentity", "Integer32", "iso", "enterprises", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
attoProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4547, 3, 2))
attoProductsMIB.setRevisions(('2013-04-19 13:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: attoProductsMIB.setRevisionsDescriptions(('Initial version of this module.',))
if mibBuilder.loadTexts: attoProductsMIB.setLastUpdated('201304191345Z')
if mibBuilder.loadTexts: attoProductsMIB.setOrganization('ATTO Technology, Inc.')
if mibBuilder.loadTexts: attoProductsMIB.setContactInfo('ATTO Technology 155 Crosspoint Parkway Amherst NY 14068 EMail: <support@attotech.com>')
if mibBuilder.loadTexts: attoProductsMIB.setDescription('This modules defines object identifiers assigned to various hardware platforms, which are returned as values for sysObjectID.')
attotech = MibIdentifier((1, 3, 6, 1, 4, 1, 4547))
attoProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1))
attoMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 2))
attoModules = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 3))
attoAgentCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 4))
attoGenericDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1, 1))
attoHba = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1, 3))
attoFB6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1, 4))
attoFB6500N = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1, 5))
mibBuilder.exportSymbols("ATTO-PRODUCTS-MIB", attoFB6500=attoFB6500, attoModules=attoModules, attotech=attotech, attoMgmt=attoMgmt, attoProductsMIB=attoProductsMIB, attoFB6500N=attoFB6500N, attoHba=attoHba, attoGenericDevice=attoGenericDevice, attoProducts=attoProducts, attoAgentCapability=attoAgentCapability, PYSNMP_MODULE_ID=attoProductsMIB)
