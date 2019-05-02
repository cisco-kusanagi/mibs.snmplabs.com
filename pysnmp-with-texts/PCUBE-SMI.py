#
# PySNMP MIB module PCUBE-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PCUBE-SMI
# Produced by pysmi-0.3.4 at Wed May  1 12:11:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, ObjectIdentity, iso, Counter32, Unsigned32, Counter64, Integer32, ModuleIdentity, TimeTicks, Gauge32, IpAddress, MibIdentifier, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ObjectIdentity", "iso", "Counter32", "Unsigned32", "Counter64", "Integer32", "ModuleIdentity", "TimeTicks", "Gauge32", "IpAddress", "MibIdentifier", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pcube = ModuleIdentity((1, 3, 6, 1, 4, 1, 5655))
pcube.setRevisions(('2002-01-14 20:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pcube.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: pcube.setLastUpdated('200201142000Z')
if mibBuilder.loadTexts: pcube.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: pcube.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-sce@cisco.com')
if mibBuilder.loadTexts: pcube.setDescription('The Structure of Management Information for the Pcube enterprise.')
pcubeProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 5655, 1))
if mibBuilder.loadTexts: pcubeProducts.setStatus('current')
if mibBuilder.loadTexts: pcubeProducts.setDescription('pcubeProducts is the root OBJECT IDENTIFIER from which sysObjectID values are assigned. Actual values are defined in PCUBE-PRODUCTS-MIB.')
pcubeModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 5655, 2))
if mibBuilder.loadTexts: pcubeModules.setStatus('current')
if mibBuilder.loadTexts: pcubeModules.setDescription('pcubeModules provides a root object identifier from which MODULE-IDENTITY values may be assigned.')
pcubeMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 5655, 3))
if mibBuilder.loadTexts: pcubeMgmt.setStatus('current')
if mibBuilder.loadTexts: pcubeMgmt.setDescription('pcubeMgmt is the main subtree for new MIB development.')
pcubeWorkgroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5655, 4))
if mibBuilder.loadTexts: pcubeWorkgroup.setStatus('current')
if mibBuilder.loadTexts: pcubeWorkgroup.setDescription("pcubeWorkgroup is the main subtree for objects and events of P-Cube's products.")
mibBuilder.exportSymbols("PCUBE-SMI", PYSNMP_MODULE_ID=pcube, pcubeMgmt=pcubeMgmt, pcubeProducts=pcubeProducts, pcubeModules=pcubeModules, pcubeWorkgroup=pcubeWorkgroup, pcube=pcube)
