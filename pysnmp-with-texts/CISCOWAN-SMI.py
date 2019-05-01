#
# PySNMP MIB module CISCOWAN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOWAN-SMI
# Produced by pysmi-0.3.4 at Wed May  1 11:34:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, Integer32, Bits, NotificationType, ObjectIdentity, enterprises, TimeTicks, Counter64, Gauge32, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "Integer32", "Bits", "NotificationType", "ObjectIdentity", "enterprises", "TimeTicks", "Counter64", "Gauge32", "MibIdentifier", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stratacom = ModuleIdentity((1, 3, 6, 1, 4, 1, 351))
stratacom.setRevisions(('2002-05-24 00:00', '2000-01-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: stratacom.setRevisionsDescriptions(("Using the 4 digit Year value in LAST-UPDATED and REVISION Clause. Modified description of 'ciscoWan'.", 'Added ciscoWanAgentCapability Object Identifier assignment.',))
if mibBuilder.loadTexts: stratacom.setLastUpdated('200205240000Z')
if mibBuilder.loadTexts: stratacom.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: stratacom.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: stratacom.setDescription('The Structure of Management Information for the stratacom enterprise.')
ciscoWan = ObjectIdentity((1, 3, 6, 1, 4, 1, 351, 150))
if mibBuilder.loadTexts: ciscoWan.setStatus('current')
if mibBuilder.loadTexts: ciscoWan.setDescription("ciscoWan is the main subtree for mibs under 'stratacom' enterprise. This is used by MGX product series.")
ciscoWanAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 351, 160))
if mibBuilder.loadTexts: ciscoWanAgentCapability.setStatus('current')
if mibBuilder.loadTexts: ciscoWanAgentCapability.setDescription('ciscoWanAgentCapability provides a root object identifier from which AGENT-CAPABILITIES values may be assigned.')
mibBuilder.exportSymbols("CISCOWAN-SMI", ciscoWanAgentCapability=ciscoWanAgentCapability, ciscoWan=ciscoWan, stratacom=stratacom, PYSNMP_MODULE_ID=stratacom)
