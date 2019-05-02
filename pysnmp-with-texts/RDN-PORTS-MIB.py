#
# PySNMP MIB module RDN-PORTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RDN-PORTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:54:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Bits, Integer32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, Counter32, Unsigned32, IpAddress, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Bits", "Integer32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "Counter32", "Unsigned32", "IpAddress", "MibIdentifier", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rdnPorts = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4, 5))
rdnPorts.setRevisions(('2008-08-08 00:00', '2005-10-20 00:00', '2003-11-05 00:00', '2003-04-29 00:00', '2001-05-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rdnPorts.setRevisionsDescriptions(("Added Copyright Statement into MIB modules's description.", 'Added definition for subinterface port', '+ Updated the CONTACT-INFO. + Reorder REVISION/DESCRIPTION in required reverse chronological order.', 'Clean up of CONTACT-INFO.', 'Initial creation.',))
if mibBuilder.loadTexts: rdnPorts.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnPorts.setOrganization('Motorola')
if mibBuilder.loadTexts: rdnPorts.setContactInfo('Motorola Customer Service 101 Tournament Drive Horsham, PA 19044 US Tel: +1 888 944 4357 Int Tel: +1 215 323 0044 Fax: +1 215 323 1502 Email: CPSSupport@Motorola.com')
if mibBuilder.loadTexts: rdnPorts.setDescription('MIB module for Motorola Port definitions. Copyright (C) 2001, 2008 by Motorola, Inc. All rights reserved.')
rdnPortsUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 0))
rdnPortsGige = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 1))
rdnPortsEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 2))
rdnPortsCableMac = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 3))
rdnPortsCableUpstream = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 4))
rdnPortsCableDownstream = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 5))
rdnPortsCableSubIf = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 6))
rdnPortsLoopback = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 7))
rdnPortsT1 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 8))
rdnPortsNull = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 9))
rdnPortsTunnel = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 10))
rdnPortsPOS = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 11))
rdnPortsATM = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 5, 12))
mibBuilder.exportSymbols("RDN-PORTS-MIB", rdnPortsCableSubIf=rdnPortsCableSubIf, rdnPortsPOS=rdnPortsPOS, rdnPorts=rdnPorts, rdnPortsLoopback=rdnPortsLoopback, rdnPortsCableUpstream=rdnPortsCableUpstream, PYSNMP_MODULE_ID=rdnPorts, rdnPortsNull=rdnPortsNull, rdnPortsT1=rdnPortsT1, rdnPortsEthernet=rdnPortsEthernet, rdnPortsCableMac=rdnPortsCableMac, rdnPortsCableDownstream=rdnPortsCableDownstream, rdnPortsUnknown=rdnPortsUnknown, rdnPortsGige=rdnPortsGige, rdnPortsATM=rdnPortsATM, rdnPortsTunnel=rdnPortsTunnel)
