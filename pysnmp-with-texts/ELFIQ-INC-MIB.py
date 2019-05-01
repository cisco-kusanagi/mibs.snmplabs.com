#
# PySNMP MIB module ELFIQ-INC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELFIQ-INC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:59:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter32, TimeTicks, Gauge32, IpAddress, NotificationType, ModuleIdentity, iso, Bits, Integer32, MibIdentifier, enterprises, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "TimeTicks", "Gauge32", "IpAddress", "NotificationType", "ModuleIdentity", "iso", "Bits", "Integer32", "MibIdentifier", "enterprises", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
elfiqInc = ModuleIdentity((1, 3, 6, 1, 4, 1, 19713))
if mibBuilder.loadTexts: elfiqInc.setLastUpdated('200811190000Z')
if mibBuilder.loadTexts: elfiqInc.setOrganization('Elfiq Inc.')
if mibBuilder.loadTexts: elfiqInc.setContactInfo(' Author: Elfiq Network postal: Montreal, QC H3B3A7 CANADA email: support@elfiq.com phone: +1-514-667-0611 ')
if mibBuilder.loadTexts: elfiqInc.setDescription('This is the standard mib of elfiq products')
elfiqMIBProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 19713, 1))
elfiqMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19713, 2))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 19713, 1, 1))
linkBalancer = MibIdentifier((1, 3, 6, 1, 4, 1, 19713, 1, 2))
commonConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19713, 2, 1))
linkBalancerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19713, 2, 2))
mibBuilder.exportSymbols("ELFIQ-INC-MIB", linkBalancerConformance=linkBalancerConformance, PYSNMP_MODULE_ID=elfiqInc, common=common, elfiqInc=elfiqInc, elfiqMIBConformance=elfiqMIBConformance, elfiqMIBProducts=elfiqMIBProducts, linkBalancer=linkBalancer, commonConformance=commonConformance)
