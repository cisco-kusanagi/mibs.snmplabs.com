#
# PySNMP MIB module FORCE10-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FORCE10-SMI
# Produced by pysmi-0.3.4 at Wed May  1 12:42:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, NotificationType, Integer32, Counter64, Gauge32, TimeTicks, Bits, IpAddress, MibIdentifier, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "NotificationType", "Integer32", "Counter64", "Gauge32", "TimeTicks", "Bits", "IpAddress", "MibIdentifier", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
force10 = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027))
force10.setRevisions(('2007-06-15 12:00', '1900-10-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: force10.setRevisionsDescriptions(('Added f10Modules.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: force10.setLastUpdated('200706151200Z')
if mibBuilder.loadTexts: force10.setOrganization('Force10 Networks, Inc.')
if mibBuilder.loadTexts: force10.setContactInfo('Force10 Networks, Inc 1440 McCarthy Blvd Milpitas, CA 95035 (408) 571-3500 support@force10networks.com http://www.force10networks.com')
if mibBuilder.loadTexts: force10.setDescription('The Structure of Management Information for the Force10 enterprise.')
f10Products = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 1))
if mibBuilder.loadTexts: f10Products.setStatus('current')
if mibBuilder.loadTexts: f10Products.setDescription("Force10 Products' OID.")
f10Common = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 2))
if mibBuilder.loadTexts: f10Common.setStatus('current')
if mibBuilder.loadTexts: f10Common.setDescription('All Force10 shared TEXTTUAL-CONVENTION definitions')
f10Mgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 3))
if mibBuilder.loadTexts: f10Mgmt.setStatus('current')
if mibBuilder.loadTexts: f10Mgmt.setDescription('f10Mgmt is the main subtree for Force10 mib development.')
f10Modules = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 4))
if mibBuilder.loadTexts: f10Modules.setStatus('current')
if mibBuilder.loadTexts: f10Modules.setDescription('f10Modules provides a root object identifier from which MODULE-IDENTITY values may be based.')
f10Experiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 20))
if mibBuilder.loadTexts: f10Experiment.setStatus('current')
if mibBuilder.loadTexts: f10Experiment.setDescription('f10Experiment provides a root object identifier from which experimental mibs may be temporarily based. mibs are typicially based here if they fall in one of two categories 1) are IETF work-in-process mibs which have not been assigned a permanent object identifier by the IANA. 2) are force10 work-in-process which has not been assigned a permanent object identifier by the force10 assigned number authority, typicially because the mib is not ready for deployment. NOTE WELL: support for mibs in the f10Experiment subtree will be deleted when a permanent object identifier assignment is made.')
mibBuilder.exportSymbols("FORCE10-SMI", force10=force10, f10Experiment=f10Experiment, f10Common=f10Common, PYSNMP_MODULE_ID=force10, f10Modules=f10Modules, f10Mgmt=f10Mgmt, f10Products=f10Products)
