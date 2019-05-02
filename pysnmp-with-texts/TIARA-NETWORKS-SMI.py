#
# PySNMP MIB module TIARA-NETWORKS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-NETWORKS-SMI
# Produced by pysmi-0.3.4 at Wed May  1 13:13:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Integer32, NotificationType, Bits, MibIdentifier, enterprises, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, IpAddress, Unsigned32, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "NotificationType", "Bits", "MibIdentifier", "enterprises", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "IpAddress", "Unsigned32", "ObjectIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tiaraNetworks = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174))
tiaraNetworks.setRevisions(('1993-04-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tiaraNetworks.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tiaraNetworks.setLastUpdated('9904230000Z')
if mibBuilder.loadTexts: tiaraNetworks.setOrganization('Tiara Networks, Inc.')
if mibBuilder.loadTexts: tiaraNetworks.setContactInfo(' Tiara Networks Customer Service Postal: 113 Fourier Ave Fremont, CA 94539 USA Tel: +1 510-360-0140 Fax: +1 510-360-0144 E-mail: cs@tiaranet.com')
if mibBuilder.loadTexts: tiaraNetworks.setDescription('The Structure of Management Information for the Tiara Networks enterprise MIB.')
tiaraProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3174, 1))
if mibBuilder.loadTexts: tiaraProducts.setStatus('current')
if mibBuilder.loadTexts: tiaraProducts.setDescription('tiaraProducts is the root OBJECT IDENTIFIER from which sysObjectID values are assigned. Actual values are defined in TIARA-PRODUCTS-MIB.')
tiaraMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 3174, 2))
if mibBuilder.loadTexts: tiaraMgmt.setStatus('current')
if mibBuilder.loadTexts: tiaraMgmt.setDescription('tiaraMgmt is the main subtree for Management groups.')
tiaraModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 3174, 3))
if mibBuilder.loadTexts: tiaraModules.setStatus('current')
if mibBuilder.loadTexts: tiaraModules.setDescription('tiaraModules provides a root object identifier from which MODULE-IDENTITY values may be assigned.')
tiaraExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 3174, 4))
if mibBuilder.loadTexts: tiaraExperiment.setStatus('current')
if mibBuilder.loadTexts: tiaraExperiment.setDescription('tiaraExperiment is the main subtree for individual groups which are used internally,not for production release. ')
tiaraInterfaces = ObjectIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 7))
if mibBuilder.loadTexts: tiaraInterfaces.setStatus('current')
if mibBuilder.loadTexts: tiaraInterfaces.setDescription('tiaraInterfaces is the main subtree for individual interface groups.')
mibBuilder.exportSymbols("TIARA-NETWORKS-SMI", tiaraInterfaces=tiaraInterfaces, PYSNMP_MODULE_ID=tiaraNetworks, tiaraMgmt=tiaraMgmt, tiaraProducts=tiaraProducts, tiaraExperiment=tiaraExperiment, tiaraNetworks=tiaraNetworks, tiaraModules=tiaraModules)
