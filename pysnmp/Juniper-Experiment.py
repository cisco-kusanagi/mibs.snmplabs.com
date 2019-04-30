#
# PySNMP MIB module Juniper-Experiment (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Experiment
# Produced by pysmi-0.3.4 at Mon Apr 29 17:08:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
juniperUniExperiment, = mibBuilder.importSymbols("Juniper-UNI-SMI", "juniperUniExperiment")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Counter64, Bits, NotificationType, Integer32, Unsigned32, MibIdentifier, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Counter64", "Bits", "NotificationType", "Integer32", "Unsigned32", "MibIdentifier", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniExperiment = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2))
juniExperiment.setRevisions(('2002-11-13 20:58', '2001-06-20 20:36', '2000-10-24 21:00',))
if mibBuilder.loadTexts: juniExperiment.setLastUpdated('200211132058Z')
if mibBuilder.loadTexts: juniExperiment.setOrganization('Juniper Networks, Inc.')
juniDvmrpExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1))
if mibBuilder.loadTexts: juniDvmrpExperiment.setStatus('current')
juniSonetApsExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2, 2))
if mibBuilder.loadTexts: juniSonetApsExperiment.setStatus('current')
juniMplsExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2, 3))
if mibBuilder.loadTexts: juniMplsExperiment.setStatus('current')
juniMplsVPNExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2, 4))
if mibBuilder.loadTexts: juniMplsVPNExperiment.setStatus('current')
juniBFDExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2, 5))
if mibBuilder.loadTexts: juniBFDExperiment.setStatus('current')
mibBuilder.exportSymbols("Juniper-Experiment", juniMplsVPNExperiment=juniMplsVPNExperiment, PYSNMP_MODULE_ID=juniExperiment, juniBFDExperiment=juniBFDExperiment, juniExperiment=juniExperiment, juniDvmrpExperiment=juniDvmrpExperiment, juniMplsExperiment=juniMplsExperiment, juniSonetApsExperiment=juniSonetApsExperiment)
