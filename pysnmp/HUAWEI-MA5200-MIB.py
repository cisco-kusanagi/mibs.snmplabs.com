#
# PySNMP MIB module HUAWEI-MA5200-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-MA5200-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:34:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
hwProducts, = mibBuilder.importSymbols("HUAWEI-MIB", "hwProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, ModuleIdentity, NotificationType, Bits, TimeTicks, Counter64, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "ModuleIdentity", "NotificationType", "Bits", "TimeTicks", "Counter64", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
musa = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 6))
if mibBuilder.loadTexts: musa.setLastUpdated('200303110900Z')
if mibBuilder.loadTexts: musa.setOrganization('Huawei Technologies Co., Ltd.')
hwMA5200Mib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6, 2))
hwMA5200G_16 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 29)).setLabel("hwMA5200G-16")
hwMA5200G_8 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 30)).setLabel("hwMA5200G-8")
hwMA5200G_4 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 31)).setLabel("hwMA5200G-4")
hwMA5200G_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 32)).setLabel("hwMA5200G-2")
hwMA5200Ifcfg = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 100))
hwMA5200L2tp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 101))
hwMA5200PPPoX = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 102))
hwMA5200Srvcfg = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 103))
mibBuilder.exportSymbols("HUAWEI-MA5200-MIB", hwMA5200L2tp=hwMA5200L2tp, hwMA5200Ifcfg=hwMA5200Ifcfg, hwMA5200G_2=hwMA5200G_2, hwMA5200PPPoX=hwMA5200PPPoX, hwMA5200G_4=hwMA5200G_4, hwMA5200G_8=hwMA5200G_8, hwMA5200G_16=hwMA5200G_16, hwMA5200Srvcfg=hwMA5200Srvcfg, musa=musa, PYSNMP_MODULE_ID=musa, hwMA5200Mib=hwMA5200Mib)
