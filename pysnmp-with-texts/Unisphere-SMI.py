#
# PySNMP MIB module Unisphere-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-SMI
# Produced by pysmi-0.3.4 at Wed May  1 12:55:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, IpAddress, MibIdentifier, enterprises, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ObjectIdentity, Counter64, iso, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "IpAddress", "MibIdentifier", "enterprises", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "iso", "Bits", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
unisphere = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874))
unisphere.setRevisions(('2001-06-01 21:46', '2000-06-01 14:30', '2000-05-24 04:00', '1999-12-13 19:36', '1999-11-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: unisphere.setRevisionsDescriptions(('Replaced OBJECT-IDENTITYs with OBJECT IDENTIFIERs.', 'Added usVoiceAdmin and usDataAdmin branchs.', 'Added node for UMC MIB', 'Added REFERENCE clauses to OBJECT-IDENTITY definitions.', 'The initial release of this management informaiton module.',))
if mibBuilder.loadTexts: unisphere.setLastUpdated('200106012146Z')
if mibBuilder.loadTexts: unisphere.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: unisphere.setContactInfo(' Unisphere Networks, Inc. Customer Service Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: info@UnisphereNetworks.com')
if mibBuilder.loadTexts: unisphere.setDescription('The Structure of Management Information for the Unisphere Networks, Inc. enterprise. This is the top-level registry for managed objects under the Unisphere Networks SNMP management enterprise object identifier.')
usProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1))
usMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2))
usVoiceMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 1))
usDataMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2))
usExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3))
usVoiceExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 1))
usDataExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2))
usAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 4))
usVoiceAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 4, 1))
usDataAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 4, 2))
usAgentCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5))
usVoiceAgents = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 1))
usDataAgents = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2))
usNetMgmtProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 6))
usUmcMib = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 6, 1))
mibBuilder.exportSymbols("Unisphere-SMI", usDataAgents=usDataAgents, usDataMibs=usDataMibs, usVoiceAgents=usVoiceAgents, usNetMgmtProducts=usNetMgmtProducts, PYSNMP_MODULE_ID=unisphere, usAgentCapability=usAgentCapability, usAdmin=usAdmin, usVoiceMibs=usVoiceMibs, unisphere=unisphere, usMibs=usMibs, usExperiment=usExperiment, usDataExperiment=usDataExperiment, usDataAdmin=usDataAdmin, usProducts=usProducts, usVoiceAdmin=usVoiceAdmin, usVoiceExperiment=usVoiceExperiment, usUmcMib=usUmcMib)
