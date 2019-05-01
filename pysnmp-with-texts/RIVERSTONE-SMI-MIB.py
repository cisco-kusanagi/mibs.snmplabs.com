#
# PySNMP MIB module RIVERSTONE-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-SMI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:57:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, NotificationType, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, TimeTicks, Counter64, ObjectIdentity, IpAddress, Integer32, Gauge32, ModuleIdentity, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "TimeTicks", "Counter64", "ObjectIdentity", "IpAddress", "Integer32", "Gauge32", "ModuleIdentity", "Counter32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
riverstoneNetworks = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567))
riverstoneNetworks.setRevisions(('2000-04-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: riverstoneNetworks.setRevisionsDescriptions(('Riverstone SMI top layer organization. ',))
if mibBuilder.loadTexts: riverstoneNetworks.setLastUpdated('200004150000Z')
if mibBuilder.loadTexts: riverstoneNetworks.setOrganization('Riverstone Networks, Inc')
if mibBuilder.loadTexts: riverstoneNetworks.setContactInfo('Riverstone Networks, Inc 5200 Great America Parkway Santa Clara CA USA 95054 PHONE:+1 408.878.6500 EMAIL: nms-eng@riverstonenet.com WEB: http://www.riverstonenet.com')
if mibBuilder.loadTexts: riverstoneNetworks.setDescription('This mib module defines the enterprise managed object space operated by Riverstone Networks, Inc http://www.riverstonenet.com/products. Copyright (C) Riverstone Networks, Inc 2000')
riverstoneProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 1))
if mibBuilder.loadTexts: riverstoneProducts.setStatus('current')
if mibBuilder.loadTexts: riverstoneProducts.setDescription('All Riverstone Product Families that include SNMP management are identified by these sysObjectIDs under this branch.')
riverstoneMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 2))
if mibBuilder.loadTexts: riverstoneMibs.setStatus('current')
if mibBuilder.loadTexts: riverstoneMibs.setDescription('All Riverstone enterprise MIBs are defined under riverstoneMibs')
riverstoneAgentCapabilities = ObjectIdentity((1, 3, 6, 1, 4, 1, 5567, 10))
if mibBuilder.loadTexts: riverstoneAgentCapabilities.setStatus('current')
if mibBuilder.loadTexts: riverstoneAgentCapabilities.setDescription('Agent Capability MIBS are defined under this branch.')
mibBuilder.exportSymbols("RIVERSTONE-SMI-MIB", riverstoneProducts=riverstoneProducts, riverstoneAgentCapabilities=riverstoneAgentCapabilities, PYSNMP_MODULE_ID=riverstoneNetworks, riverstoneMibs=riverstoneMibs, riverstoneNetworks=riverstoneNetworks)
