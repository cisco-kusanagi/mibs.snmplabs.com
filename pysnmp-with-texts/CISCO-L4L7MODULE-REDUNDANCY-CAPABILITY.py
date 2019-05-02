#
# PySNMP MIB module CISCO-L4L7MODULE-REDUNDANCY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-L4L7MODULE-REDUNDANCY-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:04:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, IpAddress, MibIdentifier, TimeTicks, Counter32, Gauge32, ModuleIdentity, iso, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "IpAddress", "MibIdentifier", "TimeTicks", "Counter32", "Gauge32", "ModuleIdentity", "iso", "Unsigned32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoL4l7moduleRedundancyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 566))
ciscoL4l7moduleRedundancyCapability.setRevisions(('2008-07-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setRevisionsDescriptions(('Added capability statement cl4l7ModRedCapc4701aceVA3R100',))
if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setLastUpdated('200807230000Z')
if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-l4l7security@cisco.com')
if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setDescription('The capabilities description for CISCO-L4L7MODULE-REDUNDANCY-MIB.')
cl4l7ModRedCapc4710aceVA3R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 566, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cl4l7ModRedCapc4710aceVA3R100 = cl4l7ModRedCapc4710aceVA3R100.setProductRelease('ACSW (Application Control Software) A3(1) for\n                     ACE 4710 Application Control Engine Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cl4l7ModRedCapc4710aceVA3R100 = cl4l7ModRedCapc4710aceVA3R100.setStatus('current')
if mibBuilder.loadTexts: cl4l7ModRedCapc4710aceVA3R100.setDescription('CISCO-L4L7-MODULE-REDUNDANCY-MIB capabilities')
mibBuilder.exportSymbols("CISCO-L4L7MODULE-REDUNDANCY-CAPABILITY", cl4l7ModRedCapc4710aceVA3R100=cl4l7ModRedCapc4710aceVA3R100, ciscoL4l7moduleRedundancyCapability=ciscoL4l7moduleRedundancyCapability, PYSNMP_MODULE_ID=ciscoL4l7moduleRedundancyCapability)
