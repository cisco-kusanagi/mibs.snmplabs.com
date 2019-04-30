#
# PySNMP MIB module CISCO-AAA-SERVER-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-AAA-SERVER-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
TimeIntervalSec, = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ModuleIdentity, Counter32, IpAddress, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, Bits, MibIdentifier, Counter64, TimeTicks, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "IpAddress", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "Bits", "MibIdentifier", "Counter64", "TimeTicks", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoAAAServerExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 372))
ciscoAAAServerExtCapability.setRevisions(('2008-06-16 00:00', '2006-02-21 00:00', '2004-08-24 00:00', '2003-11-22 00:00',))
if mibBuilder.loadTexts: ciscoAAAServerExtCapability.setLastUpdated('200806160000Z')
if mibBuilder.loadTexts: ciscoAAAServerExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoAAAServerExtCapMDS13R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 372, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapMDS13R1 = ciscoAAAServerExtCapMDS13R1.setProductRelease('Cisco MDS 1.3(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapMDS13R1 = ciscoAAAServerExtCapMDS13R1.setStatus('current')
ciscoAAAServerExtCapMDS20R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 372, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapMDS20R1 = ciscoAAAServerExtCapMDS20R1.setProductRelease('Cisco MDS 2.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapMDS20R1 = ciscoAAAServerExtCapMDS20R1.setStatus('current')
ciscoAAAServerExtCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 372, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapACSWV03R000 = ciscoAAAServerExtCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapACSWV03R000 = ciscoAAAServerExtCapACSWV03R000.setStatus('current')
ciscoAAAServerExtCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 372, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapc4710aceVA1R700 = ciscoAAAServerExtCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                        for ACE 4710 Application Control Engine \n                        Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerExtCapc4710aceVA1R700 = ciscoAAAServerExtCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-AAA-SERVER-EXT-CAPABILITY", ciscoAAAServerExtCapability=ciscoAAAServerExtCapability, ciscoAAAServerExtCapMDS20R1=ciscoAAAServerExtCapMDS20R1, PYSNMP_MODULE_ID=ciscoAAAServerExtCapability, ciscoAAAServerExtCapMDS13R1=ciscoAAAServerExtCapMDS13R1, ciscoAAAServerExtCapACSWV03R000=ciscoAAAServerExtCapACSWV03R000, ciscoAAAServerExtCapc4710aceVA1R700=ciscoAAAServerExtCapc4710aceVA1R700)
