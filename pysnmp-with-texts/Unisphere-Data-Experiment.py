#
# PySNMP MIB module Unisphere-Data-Experiment (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Experiment
# Produced by pysmi-0.3.4 at Wed May  1 12:55:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, IpAddress, MibIdentifier, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ObjectIdentity, Counter64, iso, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "IpAddress", "MibIdentifier", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "iso", "Bits", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usExperiment, = mibBuilder.importSymbols("Unisphere-SMI", "usExperiment")
usDataExperiment = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2))
usDataExperiment.setRevisions(('2001-06-20 20:36', '2000-10-24 21:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usDataExperiment.setRevisionsDescriptions(('Added OID for the SONET APS-MIB.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usDataExperiment.setLastUpdated('200106202036Z')
if mibBuilder.loadTexts: usDataExperiment.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usDataExperiment.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 Email: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usDataExperiment.setDescription('The object identifiers for experimental MIBs for the Unisphere Networks, Inc. data communications products. This is the top-level object identifier registry for SNMP modules containing experimental MIB definitions. Experimental MIBs are defined as: 1) IETF work-in-process MIBs which have not been assigned a permanent object identifier by the IANA. 2) Unisphere work-in-process MIBs that have not achieved final production quality or field experience. NOTE: Support for MIBs under the this OID subtree is temporary and changes to objects may occur without notice.')
usdDvmrpExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1))
if mibBuilder.loadTexts: usdDvmrpExperiment.setStatus('current')
if mibBuilder.loadTexts: usdDvmrpExperiment.setDescription('The object identifier used to anchor the experimental IETF draft for the Distance Vector Multicast Routing Protocol (DVMRP) MIB.')
if mibBuilder.loadTexts: usdDvmrpExperiment.setReference('IETF Inter-Domain Multicast Routing (idmr) Working Group document: draft-ietf-idmr-dvmrp-mib-11.txt.')
usdSonetApsExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2, 2))
if mibBuilder.loadTexts: usdSonetApsExperiment.setStatus('current')
if mibBuilder.loadTexts: usdSonetApsExperiment.setDescription('The object identifier used to anchor the experimental IETF draft for the SONET linear Automatic Protection Switching (APS) MIB.')
if mibBuilder.loadTexts: usdSonetApsExperiment.setReference('IETF AToM MIB (atommib) Working Group document: draft-ietf-atommib-sonetaps-mib-05.txt.')
mibBuilder.exportSymbols("Unisphere-Data-Experiment", usdSonetApsExperiment=usdSonetApsExperiment, PYSNMP_MODULE_ID=usDataExperiment, usDataExperiment=usDataExperiment, usdDvmrpExperiment=usdDvmrpExperiment)
