#
# PySNMP MIB module CISCO-VOIP-TAP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOIP-TAP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:19:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Counter64, Bits, NotificationType, IpAddress, Integer32, iso, TimeTicks, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Counter64", "Bits", "NotificationType", "IpAddress", "Integer32", "iso", "TimeTicks", "MibIdentifier", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoipTapCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 593))
ciscoVoipTapCapability.setRevisions(('2010-08-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoipTapCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoipTapCapability.setLastUpdated('201008240000Z')
if mibBuilder.loadTexts: ciscoVoipTapCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoipTapCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-li@cisco.com')
if mibBuilder.loadTexts: ciscoVoipTapCapability.setDescription('The capabilities description of CISCO-VOIP-TAP-MIB.')
ciscoVoipTapCapV15R01SXE31ASR1K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 593, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoipTapCapV15R01SXE31ASR1K = ciscoVoipTapCapV15R01SXE31ASR1K.setProductRelease('Cisco IOS XE 15.0(01)SXE31 on ASR 1000 \n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoipTapCapV15R01SXE31ASR1K = ciscoVoipTapCapV15R01SXE31ASR1K.setStatus('current')
if mibBuilder.loadTexts: ciscoVoipTapCapV15R01SXE31ASR1K.setDescription('CISCO-VOIP-TAP-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VOIP-TAP-CAPABILITY", PYSNMP_MODULE_ID=ciscoVoipTapCapability, ciscoVoipTapCapability=ciscoVoipTapCapability, ciscoVoipTapCapV15R01SXE31ASR1K=ciscoVoipTapCapV15R01SXE31ASR1K)
