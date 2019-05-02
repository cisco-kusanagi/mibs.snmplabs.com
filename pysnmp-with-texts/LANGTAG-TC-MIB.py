#
# PySNMP MIB module LANGTAG-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LANGTAG-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:56:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Counter32, Counter64, Unsigned32, NotificationType, MibIdentifier, Integer32, mib_2, Bits, Gauge32, ObjectIdentity, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Counter32", "Counter64", "Unsigned32", "NotificationType", "MibIdentifier", "Integer32", "mib-2", "Bits", "Gauge32", "ObjectIdentity", "IpAddress", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
langTagTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 165))
langTagTcMIB.setRevisions(('2007-11-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: langTagTcMIB.setRevisionsDescriptions(('Initial revision, published as RFC 5131. Copyright (C) The IETF Trust (2007). This version of this MIB module is part of RFC 5131; see the RFC itself for full legal notices.',))
if mibBuilder.loadTexts: langTagTcMIB.setLastUpdated('200711090000Z')
if mibBuilder.loadTexts: langTagTcMIB.setOrganization('IETF Operations and Management (OPS) Area')
if mibBuilder.loadTexts: langTagTcMIB.setContactInfo('EMail: ops-area@ietf.org Home page: http://www.ops.ietf.org/')
if mibBuilder.loadTexts: langTagTcMIB.setDescription('This MIB module defines a textual convention for representing BCP 47 language tags.')
class LangTag(TextualConvention, OctetString):
    reference = 'RFC 4646 BCP 47'
    description = "A language tag, constructed in accordance with BCP 47. Only lowercase characters are allowed. The purpose of this restriction is to provide unique language tags for use as indexes. BCP 47 recommends case conventions for user interfaces, but objects using this TEXTUAL-CONVENTION MUST use only lowercase. Values MUST be well-formed language tags, in conformance with the definition of well-formed tags in BCP 47. An implementation MAY further limit the values it accepts to those permitted by a 'validating' processor, as defined in BCP 47. In theory, BCP 47 language tags are of unlimited length. The language tag described in this TEXTUAL-CONVENTION is of limited length. The analysis of language tag lengths in BCP 47 confirms that this limit will not pose a problem in practice. In particular, this length is greater than the minimum requirements set out in Section 4.3.1. A zero-length language tag is not a valid language tag. This can be used to express 'language tag absent' where required, for example, when used as an index field."
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 63), )
mibBuilder.exportSymbols("LANGTAG-TC-MIB", PYSNMP_MODULE_ID=langTagTcMIB, LangTag=LangTag, langTagTcMIB=langTagTcMIB)
