#
# PySNMP MIB module ELTEX-MES-TUNING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-TUNING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:47:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, MibIdentifier, Bits, Counter64, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, NotificationType, ModuleIdentity, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "MibIdentifier", "Bits", "Counter64", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Integer32", "iso")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
eltMesTuning = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29))
eltMesTuning.setRevisions(('2014-12-19 00:00',))
if mibBuilder.loadTexts: eltMesTuning.setLastUpdated('201412190000Z')
if mibBuilder.loadTexts: eltMesTuning.setOrganization('Eltex Ltd.')
eltMesTcamTuning = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29, 1))
eltMaxSelectiveQinqIngressRules = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMaxSelectiveQinqIngressRules.setStatus('current')
eltMaxSelectiveQinqIngressRulesAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMaxSelectiveQinqIngressRulesAfterReset.setStatus('current')
eltMaxSelectiveQinqEgressRules = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMaxSelectiveQinqEgressRules.setStatus('current')
eltMaxSelectiveQinqEgressRulesAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMaxSelectiveQinqEgressRulesAfterReset.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-TUNING-MIB", eltMaxSelectiveQinqIngressRulesAfterReset=eltMaxSelectiveQinqIngressRulesAfterReset, eltMaxSelectiveQinqEgressRulesAfterReset=eltMaxSelectiveQinqEgressRulesAfterReset, PYSNMP_MODULE_ID=eltMesTuning, eltMesTuning=eltMesTuning, eltMaxSelectiveQinqIngressRules=eltMaxSelectiveQinqIngressRules, eltMaxSelectiveQinqEgressRules=eltMaxSelectiveQinqEgressRules, eltMesTcamTuning=eltMesTcamTuning)
