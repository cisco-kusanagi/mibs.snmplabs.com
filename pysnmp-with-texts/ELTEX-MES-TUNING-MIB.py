#
# PySNMP MIB module ELTEX-MES-TUNING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-TUNING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:02:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, NotificationType, ObjectIdentity, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Bits, iso, Counter32, Integer32, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Bits", "iso", "Counter32", "Integer32", "IpAddress", "Gauge32")
TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
eltMesTuning = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29))
eltMesTuning.setRevisions(('2014-12-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltMesTuning.setRevisionsDescriptions(('Added eltMesTcamTuning.',))
if mibBuilder.loadTexts: eltMesTuning.setLastUpdated('201412190000Z')
if mibBuilder.loadTexts: eltMesTuning.setOrganization('Eltex Ltd.')
if mibBuilder.loadTexts: eltMesTuning.setContactInfo('eltex.nsk.ru')
if mibBuilder.loadTexts: eltMesTuning.setDescription('The private MIB module definition for Eltex device tuning MIB.')
eltMesTcamTuning = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29, 1))
eltMaxSelectiveQinqIngressRules = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMaxSelectiveQinqIngressRules.setStatus('current')
if mibBuilder.loadTexts: eltMaxSelectiveQinqIngressRules.setDescription('Maximal number of ingress Selective QinQ rules supported.')
eltMaxSelectiveQinqIngressRulesAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMaxSelectiveQinqIngressRulesAfterReset.setStatus('current')
if mibBuilder.loadTexts: eltMaxSelectiveQinqIngressRulesAfterReset.setDescription('Future Maximal number of ingress Selective QinQ rules supported.')
eltMaxSelectiveQinqEgressRules = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMaxSelectiveQinqEgressRules.setStatus('current')
if mibBuilder.loadTexts: eltMaxSelectiveQinqEgressRules.setDescription('Maximal number of egress Selective QinQ rules supported.')
eltMaxSelectiveQinqEgressRulesAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMaxSelectiveQinqEgressRulesAfterReset.setStatus('current')
if mibBuilder.loadTexts: eltMaxSelectiveQinqEgressRulesAfterReset.setDescription('Future Maximal number of egress Selective QinQ rules supported.')
mibBuilder.exportSymbols("ELTEX-MES-TUNING-MIB", eltMaxSelectiveQinqEgressRulesAfterReset=eltMaxSelectiveQinqEgressRulesAfterReset, eltMesTcamTuning=eltMesTcamTuning, eltMaxSelectiveQinqIngressRulesAfterReset=eltMaxSelectiveQinqIngressRulesAfterReset, eltMaxSelectiveQinqIngressRules=eltMaxSelectiveQinqIngressRules, eltMaxSelectiveQinqEgressRules=eltMaxSelectiveQinqEgressRules, PYSNMP_MODULE_ID=eltMesTuning, eltMesTuning=eltMesTuning)
