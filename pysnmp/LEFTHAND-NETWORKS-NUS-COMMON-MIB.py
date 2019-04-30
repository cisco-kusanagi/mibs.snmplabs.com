#
# PySNMP MIB module LEFTHAND-NETWORKS-NUS-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LEFTHAND-NETWORKS-NUS-COMMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:55:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
lhnNusCommonMIB, lhnModules = mibBuilder.importSymbols("LEFTHAND-NETWORKS-GLOBAL-REG", "lhnNusCommonMIB", "lhnModules")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, Unsigned32, Counter32, Counter64, ObjectIdentity, Bits, NotificationType, Integer32, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Counter32", "Counter64", "ObjectIdentity", "Bits", "NotificationType", "Integer32", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
leftHandNetworksNusCommonModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9804, 1, 1, 2))
if mibBuilder.loadTexts: leftHandNetworksNusCommonModule.setLastUpdated('200106010000Z')
if mibBuilder.loadTexts: leftHandNetworksNusCommonModule.setOrganization('LeftHand Networks, Inc.')
lhnNusCommonConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1))
lhnNusCommonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 1))
lhnNusCommonCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 2))
lhnNusCommonObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2))
lhnNusCommonInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1))
lhnNusCommonNetwork = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2))
lhnNusCommonDNS = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3))
lhnNusCommonStorage = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4))
lhnNusCommonNTP = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 5))
lhnNusCommonNIS = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 6))
lhnNusCommonAEBS = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 7))
lhnNusCommonShares = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 8))
lhnNusCommonNTDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 9))
lhnNusCommonSysOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 10))
lhnNusCommonSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11))
lhnNusCommonClustering = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12))
lhnNusCommonNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13))
lhnNusCommonStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99))
lhnNusCommonEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 3))
lhnNusCommonBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 1, 1)).setObjects(("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonInfo"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNetwork"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonDNS"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonStorage"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNTP"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNIS"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonAEBS"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonShares"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNTDomain"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonSysOptions"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonSecurity"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonClustering"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonNotification"), ("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lhnNusCommonBasicGroup = lhnNusCommonBasicGroup.setStatus('current')
lhnNusCommonComplianceV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 2, 1)).setObjects(("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lhnNusCommonComplianceV1 = lhnNusCommonComplianceV1.setStatus('current')
mibBuilder.exportSymbols("LEFTHAND-NETWORKS-NUS-COMMON-MIB", lhnNusCommonShares=lhnNusCommonShares, lhnNusCommonObjs=lhnNusCommonObjs, lhnNusCommonNTP=lhnNusCommonNTP, lhnNusCommonAEBS=lhnNusCommonAEBS, lhnNusCommonSysOptions=lhnNusCommonSysOptions, lhnNusCommonInfo=lhnNusCommonInfo, lhnNusCommonStatus=lhnNusCommonStatus, lhnNusCommonNotification=lhnNusCommonNotification, lhnNusCommonComplianceV1=lhnNusCommonComplianceV1, PYSNMP_MODULE_ID=leftHandNetworksNusCommonModule, lhnNusCommonStorage=lhnNusCommonStorage, leftHandNetworksNusCommonModule=leftHandNetworksNusCommonModule, lhnNusCommonNTDomain=lhnNusCommonNTDomain, lhnNusCommonNetwork=lhnNusCommonNetwork, lhnNusCommonBasicGroup=lhnNusCommonBasicGroup, lhnNusCommonGroups=lhnNusCommonGroups, lhnNusCommonNIS=lhnNusCommonNIS, lhnNusCommonEvents=lhnNusCommonEvents, lhnNusCommonClustering=lhnNusCommonClustering, lhnNusCommonSecurity=lhnNusCommonSecurity, lhnNusCommonConfs=lhnNusCommonConfs, lhnNusCommonDNS=lhnNusCommonDNS, lhnNusCommonCompl=lhnNusCommonCompl)
