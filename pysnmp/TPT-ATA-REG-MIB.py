#
# PySNMP MIB module TPT-ATA-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-ATA-REG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:18:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibIdentifier, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, TimeTicks, Unsigned32, iso, ObjectIdentity, Counter32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "TimeTicks", "Unsigned32", "iso", "ObjectIdentity", "Counter32", "Bits", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_reg, = mibBuilder.importSymbols("TIPPINGPOINT-REG-MIB", "tpt-reg")
tpt_ata_family = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10)).setLabel("tpt-ata-family")
tpt_ata_family.setRevisions(('2016-05-25 18:54', '2015-07-30 17:35',))
if mibBuilder.loadTexts: tpt_ata_family.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_ata_family.setOrganization('Trend Micro, Inc.')
tpt_model_ata_network = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 1)).setLabel("tpt-model-ata-network")
if mibBuilder.loadTexts: tpt_model_ata_network.setStatus('current')
tpt_model_ata_mail = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 2)).setLabel("tpt-model-ata-mail")
if mibBuilder.loadTexts: tpt_model_ata_mail.setStatus('current')
mibBuilder.exportSymbols("TPT-ATA-REG-MIB", tpt_model_ata_network=tpt_model_ata_network, tpt_model_ata_mail=tpt_model_ata_mail, PYSNMP_MODULE_ID=tpt_ata_family, tpt_ata_family=tpt_ata_family)
