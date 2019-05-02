#
# PySNMP MIB module ACCEDIAN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ACCEDIAN-SMI
# Produced by pysmi-0.3.4 at Wed May  1 11:12:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, ObjectIdentity, Counter32, NotificationType, Integer32, iso, MibIdentifier, ModuleIdentity, Gauge32, TimeTicks, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ObjectIdentity", "Counter32", "NotificationType", "Integer32", "iso", "MibIdentifier", "ModuleIdentity", "Gauge32", "TimeTicks", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
accedianMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420))
accedianMIB.setRevisions(('2006-08-06 01:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: accedianMIB.setRevisionsDescriptions(('Initial version of MIB module ACCEDIAN-SMI.',))
if mibBuilder.loadTexts: accedianMIB.setLastUpdated('200608060100Z')
if mibBuilder.loadTexts: accedianMIB.setOrganization('Accedian Networks, Inc.')
if mibBuilder.loadTexts: accedianMIB.setContactInfo('Accedian Technical Assistance Center Accedian Networks, Inc. 4878 Levy, suite 202 Saint-Laurent, Quebec Canada H4R 2P1 E-mail: support@accedian.com')
if mibBuilder.loadTexts: accedianMIB.setDescription('The Structure of Management Information for Accedian Networks.')
acdProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 22420, 1))
if mibBuilder.loadTexts: acdProducts.setStatus('current')
if mibBuilder.loadTexts: acdProducts.setDescription("The root of Accedian's Product OIDs.")
acdMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 22420, 2))
if mibBuilder.loadTexts: acdMibs.setStatus('current')
if mibBuilder.loadTexts: acdMibs.setDescription("The root of Accedian's MIB objects.")
acdTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 22420, 3))
if mibBuilder.loadTexts: acdTraps.setStatus('current')
if mibBuilder.loadTexts: acdTraps.setDescription("The root of Accedian's Trap OIDs.")
acdExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 4))
acdServices = ObjectIdentity((1, 3, 6, 1, 4, 1, 22420, 5))
if mibBuilder.loadTexts: acdServices.setStatus('current')
if mibBuilder.loadTexts: acdServices.setDescription("The root of Accedian's Services OIDs.")
mibBuilder.exportSymbols("ACCEDIAN-SMI", accedianMIB=accedianMIB, acdExperiment=acdExperiment, acdMibs=acdMibs, PYSNMP_MODULE_ID=accedianMIB, acdServices=acdServices, acdTraps=acdTraps, acdProducts=acdProducts)
