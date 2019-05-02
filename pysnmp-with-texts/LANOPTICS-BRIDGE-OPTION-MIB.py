#
# PySNMP MIB module LANOPTICS-BRIDGE-OPTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LANOPTICS-BRIDGE-OPTION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:05:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Bits, Unsigned32, Counter64, NotificationType, ModuleIdentity, IpAddress, Counter32, MibIdentifier, ObjectIdentity, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Bits", "Unsigned32", "Counter64", "NotificationType", "ModuleIdentity", "IpAddress", "Counter32", "MibIdentifier", "ObjectIdentity", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lanOptics = MibIdentifier((1, 3, 6, 1, 4, 1, 224))
lanOpticsBridgeProxyAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 6))
lanOpticsLMGRAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 6, 8))
lanOpticsLMGRLinkID = MibScalar((1, 3, 6, 1, 4, 1, 224, 6, 8, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanOpticsLMGRLinkID.setStatus('mandatory')
if mibBuilder.loadTexts: lanOpticsLMGRLinkID.setDescription('When LMGR session is active with PCRouter card through PCBus - this variable gives the LRM Session Link Number (0-3) between the Host (SNMP agent) and the PCRouter LAN Reporting Mechanism.')
lanOpticsLMGRCaptCntrlLink = MibScalar((1, 3, 6, 1, 4, 1, 224, 6, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanOpticsLMGRCaptCntrlLink.setStatus('mandatory')
if mibBuilder.loadTexts: lanOpticsLMGRCaptCntrlLink.setDescription("When LMGR session is active with PCRouter card through PCBus - this variable is by default enabled (1). It means that the Host (SNMP Agent) tries to link to the LRM with the Control Link (id = 0). If this MIB variable is disabled the Host tries to establish a session with the LRM through other links, and if succeeds, it doesn't try to capture link 0.")
mibBuilder.exportSymbols("LANOPTICS-BRIDGE-OPTION-MIB", lanOpticsLMGRAgent=lanOpticsLMGRAgent, lanOpticsLMGRCaptCntrlLink=lanOpticsLMGRCaptCntrlLink, lanOptics=lanOptics, lanOpticsLMGRLinkID=lanOpticsLMGRLinkID, lanOpticsBridgeProxyAgent=lanOpticsBridgeProxyAgent)
