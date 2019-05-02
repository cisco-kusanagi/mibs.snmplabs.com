#
# PySNMP MIB module IANAPowerStateSet-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANAPowerStateSet-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:02:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter32, TimeTicks, iso, IpAddress, Counter64, NotificationType, Unsigned32, Bits, Integer32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "TimeTicks", "iso", "IpAddress", "Counter64", "NotificationType", "Unsigned32", "Bits", "Integer32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "mib-2")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaPowerStateSet = ModuleIdentity((1, 3, 6, 1, 2, 1, 228))
ianaPowerStateSet.setRevisions(('2015-02-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaPowerStateSet.setRevisionsDescriptions(('Initial version of this MIB module, as published as RFC 7460.',))
if mibBuilder.loadTexts: ianaPowerStateSet.setLastUpdated('201502090000Z')
if mibBuilder.loadTexts: ianaPowerStateSet.setOrganization('IANA')
if mibBuilder.loadTexts: ianaPowerStateSet.setContactInfo(' Internet Assigned Numbers Authority Postal: ICANN 12025 Waterfront Drive, Suite 300 Los Angeles, CA 90094 United States Tel: +1-310-301 5800 EMail: iana@iana.org')
if mibBuilder.loadTexts: ianaPowerStateSet.setDescription("Copyright (c) 2015 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info). This MIB module defines the PowerStateSet Textual Convention, which specifies the Power State Sets and Power State Set Values an Energy Object supports. The initial version of this MIB module was published in RFC 7460; for full legal notices see the RFC itself.")
class PowerStateSet(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/power-state-sets'
    description = 'IANAPowerState is a textual convention that describes Power State Sets and Power State Set Values an Energy Object supports. IANA has created a registry of Power State supported by an Energy Object and IANA shall administer the list of Power State Sets and Power States. The Textual Convention assumes that Power States in a Power State Set are limited to 255 distinct values. For a Power State Set S, the named number with the value S * 256 is allocated to indicate the Power State Set. For a Power State X in the Power State Set S, the named number with the value S * 256 + X + 1 is allocated to represent the Power State. Requests for new values should be made to IANA via email (iana@iana.org).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 255, 256, 257, 258, 259, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036))
    namedValues = NamedValues(("other", 0), ("unknown", 255), ("ieee1621", 256), ("ieee1621Off", 257), ("ieee1621Sleep", 258), ("ieee1621On", 259), ("dmtf", 512), ("dmtfOn", 513), ("dmtfSleepLight", 514), ("dmtfSleepDeep", 515), ("dmtfOffHard", 516), ("dmtfOffSoft", 517), ("dmtfHibernate", 518), ("dmtfPowerOffSoft", 519), ("dmtfPowerOffHard", 520), ("dmtfMasterBusReset", 521), ("dmtfDiagnosticInterrapt", 522), ("dmtfOffSoftGraceful", 523), ("dmtfOffHardGraceful", 524), ("dmtfMasterBusResetGraceful", 525), ("dmtfPowerCycleOffSoftGraceful", 526), ("dmtfPowerCycleHardGraceful", 527), ("eman", 1024), ("emanMechOff", 1025), ("emanSoftOff", 1026), ("emanHibernate", 1027), ("emanSleep", 1028), ("emanStandby", 1029), ("emanReady", 1030), ("emanLowMinus", 1031), ("emanLow", 1032), ("emanMediumMinus", 1033), ("emanMedium", 1034), ("emanHighMinus", 1035), ("emanHigh", 1036))

mibBuilder.exportSymbols("IANAPowerStateSet-MIB", ianaPowerStateSet=ianaPowerStateSet, PYSNMP_MODULE_ID=ianaPowerStateSet, PowerStateSet=PowerStateSet)
