#
# PySNMP MIB module SNMP-IEEE802-TM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-IEEE802-TM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:08:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, MibIdentifier, Gauge32, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, snmpDomains, TimeTicks, snmpModules, Integer32, ObjectIdentity, Bits, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "MibIdentifier", "Gauge32", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "snmpDomains", "TimeTicks", "snmpModules", "Integer32", "ObjectIdentity", "Bits", "iso", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snmpIeee802TmMib = ModuleIdentity((1, 3, 6, 1, 6, 3, 21))
snmpIeee802TmMib.setRevisions(('2006-11-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snmpIeee802TmMib.setRevisionsDescriptions(('The initial version, published as RFC 4789.',))
if mibBuilder.loadTexts: snmpIeee802TmMib.setLastUpdated('200611210000Z')
if mibBuilder.loadTexts: snmpIeee802TmMib.setOrganization('IETF Operations and Management Area')
if mibBuilder.loadTexts: snmpIeee802TmMib.setContactInfo('Juergen Schoenwaelder (Editor) International University Bremen P.O. Box 750 561 28725 Bremen, Germany Phone: +49 421 200-3587 EMail: j.schoenwaelder@iu-bremen.de Send comments to <ietfmibs@ops.ietf.org>.')
if mibBuilder.loadTexts: snmpIeee802TmMib.setDescription('This MIB module defines the SNMP over IEEE 802 transport mapping. Copyright (C) The IETF Trust (2006). This version of this MIB module is part of RFC 4789; see the RFC itself for full legal notices.')
snmpIeee802Domain = ObjectIdentity((1, 3, 6, 1, 6, 1, 6))
if mibBuilder.loadTexts: snmpIeee802Domain.setStatus('current')
if mibBuilder.loadTexts: snmpIeee802Domain.setDescription('The SNMP over IEEE 802 networks transport domain. The corresponding transport address is of type MacAddress as defined in the SNMPv2-TC module (RFC 2579).')
if mibBuilder.loadTexts: snmpIeee802Domain.setReference('RFC 2579')
mibBuilder.exportSymbols("SNMP-IEEE802-TM-MIB", snmpIeee802Domain=snmpIeee802Domain, snmpIeee802TmMib=snmpIeee802TmMib, PYSNMP_MODULE_ID=snmpIeee802TmMib)
