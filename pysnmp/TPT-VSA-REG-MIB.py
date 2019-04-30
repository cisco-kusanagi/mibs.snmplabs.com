#
# PySNMP MIB module TPT-VSA-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-VSA-REG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, Bits, TimeTicks, Gauge32, Counter32, NotificationType, Counter64, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Bits", "TimeTicks", "Gauge32", "Counter32", "NotificationType", "Counter64", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tpt_products, tpt_reg = mibBuilder.importSymbols("TIPPINGPOINT-REG-MIB", "tpt-products", "tpt-reg")
tpt_vsaMIBs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 10)).setLabel("tpt-vsaMIBs")
tpt_vsaMIBs.setRevisions(('2016-05-25 18:54', '2014-11-11 19:37',))
if mibBuilder.loadTexts: tpt_vsaMIBs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_vsaMIBs.setOrganization('Trend Micro, Inc.')
tpt_vsa_family = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10)).setLabel("tpt-vsa-family")
if mibBuilder.loadTexts: tpt_vsa_family.setStatus('current')
tpt_model_V10F = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 1)).setLabel("tpt-model-V10F")
if mibBuilder.loadTexts: tpt_model_V10F.setStatus('current')
tpt_model_V1000F = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 2)).setLabel("tpt-model-V1000F")
if mibBuilder.loadTexts: tpt_model_V1000F.setStatus('current')
tpt_model_V2000F = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 3)).setLabel("tpt-model-V2000F")
if mibBuilder.loadTexts: tpt_model_V2000F.setStatus('current')
tpt_model_V5000F = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 4)).setLabel("tpt-model-V5000F")
if mibBuilder.loadTexts: tpt_model_V5000F.setStatus('current')
mibBuilder.exportSymbols("TPT-VSA-REG-MIB", tpt_model_V10F=tpt_model_V10F, tpt_vsaMIBs=tpt_vsaMIBs, tpt_model_V1000F=tpt_model_V1000F, PYSNMP_MODULE_ID=tpt_vsaMIBs, tpt_model_V5000F=tpt_model_V5000F, tpt_model_V2000F=tpt_model_V2000F, tpt_vsa_family=tpt_vsa_family)
