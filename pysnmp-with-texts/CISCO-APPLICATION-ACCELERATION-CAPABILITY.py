#
# PySNMP MIB module CISCO-APPLICATION-ACCELERATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-APPLICATION-ACCELERATION-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:50:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Integer32, Gauge32, MibIdentifier, ModuleIdentity, Counter64, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, IpAddress, TimeTicks, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "MibIdentifier", "ModuleIdentity", "Counter64", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "IpAddress", "TimeTicks", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoAppAccCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 567))
ciscoAppAccCapability.setRevisions(('2008-07-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAppAccCapability.setRevisionsDescriptions(('Added capability statement ciscoAppAccCapc4710aceVA1R700 for ACE 4710 Application Control Engine Appliance.',))
if mibBuilder.loadTexts: ciscoAppAccCapability.setLastUpdated('200807290000Z')
if mibBuilder.loadTexts: ciscoAppAccCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAppAccCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-avs@cisco.com')
if mibBuilder.loadTexts: ciscoAppAccCapability.setDescription('The capabilities description of CISCO-APPLICATION-ACCELERATION-MIB.')
ciscoAppAccCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 567, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppAccCapc4710aceVA1R700 = ciscoAppAccCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7) for ACE \n                4710 Application Control Engine Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppAccCapc4710aceVA1R700 = ciscoAppAccCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoAppAccCapc4710aceVA1R700.setDescription('CISCO-APPLICATION-ACCELERATION-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-APPLICATION-ACCELERATION-CAPABILITY", PYSNMP_MODULE_ID=ciscoAppAccCapability, ciscoAppAccCapc4710aceVA1R700=ciscoAppAccCapc4710aceVA1R700, ciscoAppAccCapability=ciscoAppAccCapability)
